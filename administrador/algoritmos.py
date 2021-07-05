import math
from queue import PriorityQueue
from PySide2.QtGui import QPen,QColor


def distancia_euclidiana(x_1, y_1 , x_2, y_2) :
    raiz = math.sqrt((x_2 - x_1)**2 + (y_2-y_1)**2)
    return raiz

def recorrido_profundidad(inicio, diccionario) :

    visitados = []
    pila = []
    recorrido = []

    visitados.append(inicio)
    pila.append(inicio)

    while len(pila) > 0 :

        ultimo = pila[-1]
        recorrido.append(ultimo)
      
        lista = list(diccionario[ultimo])
        adyacente = []
        for p in lista :
            adyacente.append(p[0])
        pila.pop()
        for p in adyacente :
            if not p in visitados :
                pila.append(p)
        
        for p in adyacente :
            if not p in visitados :
                visitados.append(p)
    return recorrido

def recorrido_amplitud(inicio, diccionario) :

    visitados = []
    pila = []
    recorrido = []

    visitados.append(inicio)
    pila.append(inicio)

    while len(pila) > 0 :

        ultimo = pila[0]
        recorrido.append(ultimo)
      
        lista = list(diccionario[ultimo])
        adyacente = []
        for p in lista :
            adyacente.append(p[0])
        pila.pop(0)
        for p in adyacente :
            if not p in visitados :
                pila.append(p)
        
        for p in adyacente :
            if not p in visitados :
                visitados.append(p)
    return recorrido

def recorrido_amplitud(inicio,diccionario) :
    visitados = []
    pila = []
    recorrido = []

    visitados.append(inicio)
    pila.append(inicio)

    while len(pila) > 0 :

        ultimo = pila[-1]
        recorrido.append(ultimo)
      
        lista = list(diccionario[ultimo])
        adyacente = []
        for p in lista :
            adyacente.append(p[0])
        pila.pop()
        for p in adyacente :
            if not p in visitados :
                pila.append(p)
        
        for p in adyacente :
            if not p in visitados :
                visitados.append(p)
    return recorrido


def algoritmo_prim(origen, diccionario, self) :

    visitados = []
    visitados.append(origen)
    pen = QPen()
    pen.setWidth(2)
    color = QColor(150,50,150)
    pen.setColor(color)
    pq = PriorityQueue()

    lista = list(diccionario[origen])

    for p in lista :
        aristas = (p[1],p[0]) #Posicion 0 = arista Posicion 1 = ponderacion
        pq.put(aristas)

    destino = pq.get()
    destino = destino[1]

    while not pq.empty() :
        
        if not destino in visitados :
            lista = list(diccionario[destino]) #Posicion 0 = arista Posicion 1 = podenracion
            visitados.append(destino)
            for p in lista :
                if p[0] not in visitados :
                    value = (p[1],p[0])
                    pq.put(value)

            destino1 = pq.get()
            destino = destino1[1]
            distancia = destino1[0]
            print(destino, str(distancia))
            for value in self.particulas :
                if value.distancia == distancia :
                    destino_x = destino[0]
                    destino_y = destino[1]
                    self.scene.addLine(value.origen_x+3,value.origen_y+3,destino_x,destino_y,pen)
        else :
            pq.get()
            pq_copy = PriorityQueue()
            if not pq.empty() :
                while not pq.empty() :
                    value = pq.get()
                    pq_copy.put(value)
                pq = pq_copy
                destino = pq_copy.get()
                destino = destino[1]
    return visitados