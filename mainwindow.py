from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem,QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen,QColor
from ui_mainwindow import Ui_MainWindow
from administrador.particula import Particula
from administrador.particulas import Particulas
from pprint import pformat
from administrador.algoritmos import recorrido_profundidad, recorrido_amplitud, algoritmo_prim, distancia_euclidiana


class Mainwindow(QMainWindow) :
    def __init__(self) :
        super(Mainwindow, self).__init__()
        self.particulas = Particulas()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.action_guardar.triggered.connect(self.guardar_archivo)
        self.ui.action_abrir.triggered.connect(self.abrir_archivo)
        #Tabla :
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_tabla_pushButton.clicked.connect(self.buscar_tabla)
        #Grafica:
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.ui.dibujar_pushButton.clicked.connect(self.dibujar_grafica)
        self.ui.limpiar_pushButton.clicked.connect(self.limpiar_grafica)
        #Ordenar Lista :
        self.ui.id_ascendente_pushButton.clicked.connect(self.click_id_ascendente)
        self.ui.distancia_descendente_pushButton.clicked.connect(self.click_distancia_descendente)
        self.ui.velocidad_ascendente_pushButton.clicked.connect(self.click_velocidad_ascendente)
        #Algoritmos
        self.ui.action_busqueda_profundidad_y_amplitud.triggered.connect(self.busqueda_profundidad_y_amplitud)
        self.ui.action_algoritmo_prim.triggered.connect(self.algoritmo_prim)
 

    @Slot()
    def click_id_ascendente(self) :
        self.particulas.id_ascendente()
        imprimir_tabla(self)
    @Slot()
    def click_distancia_descendente(self) :
        self.particulas.distancia_descendente()
        imprimir_tabla(self)
    @Slot()
    def click_velocidad_ascendente(self) :
        self.particulas.velocidad_ascendente()
        imprimir_tabla(self)

    def wheelEvent(self, event) :
        if event.delta() > 0 :
            self.ui.graphicsView.scale(1.2,1.2)
        else :
            self.ui.graphicsView.scale(0.8,0.8)

    @Slot()
    def dibujar_grafica(self) :
        for particula in self.particulas :
            origen_x = particula.origen_x
            origen_y = particula.origen_y
            destino_x = particula.destino_x
            destino_y = particula.destino_y
            r = particula.red
            g = particula.green
            b = particula.blue

            pen = QPen()
            pen.setWidth(2)
            color = QColor(r,g,b)
            pen.setColor(color)

            self.scene.addEllipse(origen_x, origen_y, 6,6,pen)
            self.scene.addEllipse(destino_x, destino_y, 6,6,pen)
            self.scene.addLine(origen_x+3,origen_y+3,destino_x,destino_y,pen)


    @Slot()
    def limpiar_grafica(self) :
        self.scene.clear()

    @Slot()
    def mostrar_tabla(self) :
        imprimir_tabla(self)

    @Slot()
    def buscar_tabla(self) :

        id = self.ui.buscar_tabla_lineEdit.text()
        encontrado = False

        for particula in self.particulas :

            if id == particula.id :

                self.ui.tabla.clear()
                self.ui.tabla.setColumnCount(10)
                headers = ["ID","Origen X","Origen Y","Destino en x","Destino en y","Velocidad","Red","Green","Blue","Distancia"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(particula.id)
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(particula.velocidad)
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                red_blue = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, red_blue)
                self.ui.tabla.setItem(0, 9, distancia_widget)
                encontrado = True
                break
        if not encontrado :
            QMessageBox.warning(
                self,
                'Atencion',
                f'La particula con id "{id}" no existe'
            )

    @Slot()
    def abrir_archivo(self) :
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        if self.particulas.abrir(ubicacion) :
            QMessageBox.information(
                self,
                'Exito',
                'Se abrio el archivo ' + ubicacion
            )
        else :
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo abrir el archivo'
            )

    @Slot()
    def guardar_archivo(self) :
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        
        if self.particulas.guardar(ubicacion) :
            QMessageBox.information(
                self,
                'Exito',
                'Guardado correctamente en ' + ubicacion
            )
        else :
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo guardar el archivo'
            )

    @Slot()
    def click_mostrar(self) :
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))
        diccionario = pformat(self.particulas.diccionario())
        self.ui.salida.insertPlainText(diccionario)
        
    @Slot()
    def click_agregar_final(self) :
        i_d = self.ui.id_lineEdit.text()
        origen_x  = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(i_d, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self) :
        id = self.ui.id_lineEdit.text()
        origen_x  = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_inicio(particula)

    @Slot()
    def busqueda_profundidad_y_amplitud(self) :
        diccionario = self.particulas.diccionario()
        origen = (self.ui.origen_x_spinBox.value(),self.ui.origen_y_spinBox.value())
        recorrido = pformat(recorrido_profundidad(origen,diccionario))
        recorrido15 = pformat(recorrido_amplitud(origen,diccionario))

        print('PROFUNDIDAD' + '\n', recorrido)
        print('AMPLITUD' + '\n', recorrido15)

    @Slot()
    def algoritmo_prim(self) :
        diccionario = self.particulas.diccionario()
        origen = ((self.ui.origen_x_spinBox.value(),self.ui.origen_y_spinBox.value()))
        self.scene.clear()
        recorrido = algoritmo_prim(origen, diccionario,self)
        print(recorrido)

        # for values in recorrido :
        #     punto_x = values[0]
        #     punto_y = values[1]
        #     self.scene.addEllipse(punto_x, punto_y, 6,6,pen)


def imprimir_tabla(self) :
        self.ui.tabla.setColumnCount(10)
        headers = ["ID","Origen X","Origen Y","Destino en x","Destino en y","Velocidad","Red","Green","Blue","Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.particulas))
 
        row = 0
        for particula in self.particulas :
            id_widget = QTableWidgetItem(particula.id)
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(particula.velocidad)
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            red_blue = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, red_blue)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1