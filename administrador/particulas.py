from .particula import Particula
import json

class Particulas :
    def __init__(self) :
        self.__particulas = []
    
    def agregar_final (self, particula:Particula) :
        self.__particulas.append(particula)

    def agregar_inicio (self, particula:Particula) :
        self.__particulas.insert(0, particula)

    def mostrar (self) :
        for particula in self.__particulas :
            print(particula)

    def id_ascendente(self) :
        self.__particulas.sort(key= lambda troca: troca.id)

    def distancia_descendente(self) :
        self.__particulas.sort(key= lambda particula: particula.distancia, reverse = True)

    def velocidad_ascendente(self) :
        self.__particulas.sort(key= lambda particula: particula.velocidad)   

    def __len__(self) :
        return len(self.__particulas)

    def __iter__(self) :
        self.cont = 0
        return self

    def __next__(self) :
        if self.cont < len(self.__particulas) :
            particula = self.__particulas[self.cont]
            self.cont+=1 
            return particula
        else :
             raise StopIteration
        
    def __str__(self) :
        return "".join ( str(particula) + '\n' for particula in self.__particulas)

    def guardar(self, ubicacion) :
        try :
            with open(ubicacion, 'w') as archivo :
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)

                return 1
        except: 
            return 0

    def abrir(self, ubicacion) :
        try :
            with open(ubicacion, 'r') as archivo :
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]

                return 1
        except :
            return 0

    def diccionario(self) :
        diccionario = dict()
        for valor in self.__particulas :
            origen = ((valor.origen_x,valor.origen_y))
            destino = ((valor.destino_x,valor.destino_y))
            distancia = (valor.distancia)
            arista_a_b = (destino,distancia)
            arista_b_a = (origen,distancia)

            if origen in diccionario :
                diccionario[origen].append(arista_a_b)
            else :
                diccionario[origen] = [arista_a_b]

            if destino in diccionario :
                diccionario[destino].append(arista_b_a)
            else :
                diccionario[destino] = [arista_b_a]
        return diccionario

            

            
