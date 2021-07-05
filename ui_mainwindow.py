# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(788, 486)
        self.action_abrir = QAction(MainWindow)
        self.action_abrir.setObjectName(u"action_abrir")
        self.action_guardar = QAction(MainWindow)
        self.action_guardar.setObjectName(u"action_guardar")
        self.action_busqueda_profundidad_y_amplitud = QAction(MainWindow)
        self.action_busqueda_profundidad_y_amplitud.setObjectName(u"action_busqueda_profundidad_y_amplitud")
        self.action_busqueda_amplitud = QAction(MainWindow)
        self.action_busqueda_amplitud.setObjectName(u"action_busqueda_amplitud")
        self.action_algoritmo_prim = QAction(MainWindow)
        self.action_algoritmo_prim.setObjectName(u"action_algoritmo_prim")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout.addWidget(self.id_lineEdit, 0, 1, 1, 3)

        self.salida = QPlainTextEdit(self.groupBox)
        self.salida.setObjectName(u"salida")

        self.gridLayout.addWidget(self.salida, 0, 4, 13, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)

        self.origen_x_spinBox = QSpinBox(self.groupBox)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setEnabled(True)
        self.origen_x_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origen_x_spinBox, 1, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 3)

        self.origen_y_spinBox = QSpinBox(self.groupBox)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.origen_y_spinBox, 2, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)

        self.destino_x_spinBox = QSpinBox(self.groupBox)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destino_x_spinBox, 3, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 2)

        self.destino_y_spinBox = QSpinBox(self.groupBox)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destino_y_spinBox, 4, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 2)

        self.velocidad_lineEdit = QLineEdit(self.groupBox)
        self.velocidad_lineEdit.setObjectName(u"velocidad_lineEdit")

        self.gridLayout.addWidget(self.velocidad_lineEdit, 5, 2, 1, 2)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 2)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.red_spinBox, 7, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 1, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.green_spinBox, 8, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 1, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.blue_spinBox, 9, 3, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 10, 0, 1, 4)

        self.agregar_inicio_pushButton = QPushButton(self.groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 11, 0, 1, 4)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 12, 0, 1, 4)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.buscar_tabla_pushButton = QPushButton(self.tab_2)
        self.buscar_tabla_pushButton.setObjectName(u"buscar_tabla_pushButton")
        self.buscar_tabla_pushButton.setGeometry(QRect(600, 330, 75, 23))
        self.buscar_tabla_lineEdit = QLineEdit(self.tab_2)
        self.buscar_tabla_lineEdit.setObjectName(u"buscar_tabla_lineEdit")
        self.buscar_tabla_lineEdit.setGeometry(QRect(10, 330, 571, 20))
        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")
        self.mostrar_tabla_pushButton.setGeometry(QRect(680, 330, 75, 23))
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setGeometry(QRect(9, 9, 751, 311))
        self.distancia_descendente_pushButton = QPushButton(self.tab_2)
        self.distancia_descendente_pushButton.setObjectName(u"distancia_descendente_pushButton")
        self.distancia_descendente_pushButton.setGeometry(QRect(260, 360, 241, 23))
        self.id_ascendente_pushButton = QPushButton(self.tab_2)
        self.id_ascendente_pushButton.setObjectName(u"id_ascendente_pushButton")
        self.id_ascendente_pushButton.setGeometry(QRect(10, 360, 241, 23))
        self.velocidad_ascendente_pushButton = QPushButton(self.tab_2)
        self.velocidad_ascendente_pushButton.setObjectName(u"velocidad_ascendente_pushButton")
        self.velocidad_ascendente_pushButton.setGeometry(QRect(510, 360, 241, 23))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_6.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar_pushButton = QPushButton(self.tab_3)
        self.dibujar_pushButton.setObjectName(u"dibujar_pushButton")

        self.gridLayout_6.addWidget(self.dibujar_pushButton, 1, 0, 1, 1)

        self.limpiar_pushButton = QPushButton(self.tab_3)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")
        self.limpiar_pushButton.setAutoFillBackground(False)
        self.limpiar_pushButton.setAutoDefault(False)
        self.limpiar_pushButton.setFlat(False)

        self.gridLayout_6.addWidget(self.limpiar_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 788, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.action_abrir)
        self.menuArchivo.addAction(self.action_guardar)
        self.menuAlgoritmos.addAction(self.action_busqueda_profundidad_y_amplitud)
        self.menuAlgoritmos.addAction(self.action_algoritmo_prim)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.limpiar_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_abrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.action_abrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_guardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.action_guardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_busqueda_profundidad_y_amplitud.setText(QCoreApplication.translate("MainWindow", u"Busqueda Profundidad y Aomplitud", None))
        self.action_busqueda_amplitud.setText(QCoreApplication.translate("MainWindow", u"Busqueda Amplitud", None))
        self.action_algoritmo_prim.setText(QCoreApplication.translate("MainWindow", u"Algoritmo Prim", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Registro de datos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID : ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en x : ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Origen en y : ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destino x : ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Destino y : ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Velocidad : ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color (RGB) ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"red", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"green", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"blue", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.buscar_tabla_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba la ID", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.distancia_descendente_pushButton.setText(QCoreApplication.translate("MainWindow", u"Distancia (Descendiente)", None))
        self.id_ascendente_pushButton.setText(QCoreApplication.translate("MainWindow", u"ID (Ascendente)", None))
        self.velocidad_ascendente_pushButton.setText(QCoreApplication.translate("MainWindow", u"Velocidad (Ascendente)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Grafica", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

