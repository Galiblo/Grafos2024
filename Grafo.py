from Arco import Arco
from Nodo import Nodo
import heapq
from enum import Enum

class Color(Enum):
    GRIS = 1
    BLANCO = 2
    NEGRO = 3
class Grafo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.V = {}
        self.E = []
        self.tiempo = 0

    def addNodo(self, nodo):
        """
        :param nodo: no debe ser Nodo, debe ser un str (el nombre del nodo)
        :return: void
        """
        if nodo not in self.V:
            self.V[nodo] = Nodo(nodo)

    def getNodo(self, nodo):
        """
        :param nodo: debe ser un str con el nombre del nodo
        :return: si existe un Nodo con ese nombre lo regresa; de otra forma, regresa None
        """
        return self.V.get(nodo,None)

    def addArco(self, origen, destino, costo):
        """

        :param origen: str con el nombre del Nodo origen
        :param destino: str con el nombre del Nodo destino
        :param costo: flotante con el costo del arco
        :return:
        """
        if self.getNodo(origen) is not None and self.getNodo(destino) is not None:
            arco = Arco(self.V[origen], self.V[destino], float(costo))
            self.V[origen].addAdyacente(self.V[destino])
            self.E.append(arco)


    def getArco(self,u, v):
        """

        :param u: Nodo origen
        :param v: Nodo destino
        :return: si hay un arco que uno los 2 Nodos, regresa su valor, de otra forma regresa None
        """
        for a in self.E:
            if a.origen.nombre == u and a.destino.nombre == v:
                return a
        return None

    def __str__(self):
        resultado = ""+self.nombre+"\n"
        for nodo in self.V.values():
            resultado += str(nodo) + "\n"
        return resultado

    def BFS(self,s):
        for u in self.V.values():
            u.color = Color.BLANCO
            u.d= float("Inf")
            u.padre = None
        s = self.getNodo(s)
        s.d = 0
        Q = []
        Q.append(s)
        while len(Q) > 0:
            u = Q.pop(0)
            for v in u.adyacentes:
                if v.color == Color.BLANCO:
                    v.color = Color.GRIS
                    v.d = u.d + 1
                    v.padre = u
                    Q.append(v)
            u.color = Color.NEGRO

    """
        def DFS(self,g):
        for u in self.V.values():
            u.color = Color.BLANCO
            u.padre = None
        u.tiempo = 0
        for u in self.V.values():
            if u.color == Color.BLANCO:
                u.DFS_Visit(u)

    def DFS_Visit(self, u):
        u.color = Color.GRIS
        u.d = u.tiempo = u.tiempo + 1
        for v in u.adyacentes:
            if v.color == Color.BLANCO:
                u.padre = v.padre
                v.DFS_Visit(v)
        u.color = Color.NEGRO
        u.f = u.tiempo = u.tiempo + 1
    """
    def DFS_visit(self,u, tiempo):
        u.color = Color.GRIS
        tiempo = tiempo + 1
        u.d = tiempo
        for v in u.adyacentes:
            if v.color == Color.BLANCO:
                v.padre = u
                tiempo = self.DFS_visit(v, tiempo)
        u.color = Color.NEGRO
        tiempo = tiempo + 1
        u.f = tiempo
        return tiempo
    def DFS(self):
        for u in self.V.values():
            u.color = Color.BLANCO
            u.padre = None
        tiempo = 0
        for u in self.V.values():
            if u.color == Color.BLANCO:
                tiempo = self.DFS_visit(u, tiempo)


    def getFDesc(self):
        lista = []
        lista_nodos = sorted(self.V.values(), key = lambda x:x.f, reverse=True)
        for nodo in lista_nodos:
            lista.append(nodo.nombre)
        return lista

    def getT(self):
        gt = Grafo(f"{self.nombre}_T")
        for u in self.V.values():
            gt.addNodo(u.nombre)
        for e in self.E:
            gt.addArco(e.destino.nombre, e.origen.nombre, e.costo)
        return gt

    def SCC(self):
        self.DFS()                                              #Calcular f
        gt = self.getT()                                        #Obtenemos el grafo transpuesto
        ordenDescendente = gt.getFDesc()                        #Obtenemos el orden descendente de f
        for u in gt.V.values():                                 #Inicializar colores en el grafoT
            u.color = Color.BLANCO
            u.padre = None
        tiempo = 0
        bosque = []                                             #Crear la lista bosque
        for a in ordenDescendente:                              #Iteramos GT en el orden inverso de F
            u = gt.getNodo(a)
            if u.color == Color.BLANCO:
                arbol = []
                tiempo = gt.SCC_visit(u, tiempo, arbol)
                bosque.append(arbol)
        return bosque


    def SCC_visit(self,u, tiempo, arbol):
        arbol.append(u)
        u.color = Color.GRIS
        tiempo = tiempo + 1
        u.d = tiempo
        for v in u.adyacentes:
            if v.color == Color.BLANCO:
                v.padre = u
                tiempo = self.SCC_visit(v, tiempo, arbol)
        u.color = Color.NEGRO
        tiempo = tiempo + 1
        u.f = tiempo
        return tiempo
    """
    def MST_Kruskal(self):
        A = Grafo(f"{self.nombre}_MST")
        unionFind = {}
        for iter, v in enumerate(self.V.values()):
            unionFind[v.nombre] = iter
        return unionFind
    """

    def encontrar(self, padre, i):
        while padre[i] != i:
            i = padre[i]
        return i

    def unir(self, padre, rango, x, y):
        raiz_x = self.encontrar(padre, x)
        raiz_y = self.encontrar(padre, y)

        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1

    def kruskal(self):
        arbol_minimo = []

        # Ordenar arcos por peso
        self.E.sort(key=lambda arco: arco.costo)

        padre = {}
        rango = {}

        for nodo in self.V:
            padre[nodo] = nodo
            rango[nodo] = 0

        for arco in self.E:
            origen_raiz = self.encontrar(padre, arco.origen.nombre)
            destino_raiz = self.encontrar(padre, arco.destino.nombre)

            if origen_raiz != destino_raiz:
                arbol_minimo.append(arco)
                self.unir(padre, rango, origen_raiz, destino_raiz)

        return arbol_minimo

    def imprimir_arbol_minimo(self, arbol_minimo):
        info_nodos = {}
        for arco in arbol_minimo:
            origen_info = f"{arco.origen.nombre}, d({arco.origen.d}), f({arco.origen.f}), p({arco.origen.padre.nombre if arco.origen.padre else ''}), {arco.origen.color}, id({arco.origen.id})"
            destino_info = f"{arco.destino.nombre}, d({arco.destino.d}), f({arco.destino.f}), p({arco.destino.padre.nombre if arco.destino.padre else ''}), {arco.destino.color}, id({arco.destino.id})"

            if origen_info in info_nodos:
                info_nodos[origen_info].append(arco.destino.nombre)
            else:
                info_nodos[origen_info] = [arco.destino.nombre]

            if destino_info in info_nodos:
                info_nodos[destino_info].append(arco.origen.nombre)
            else:
                info_nodos[destino_info] = [arco.origen.nombre]

        for info, adyacentes in info_nodos.items():
            adyacentes_str = ", ".join(adyacentes)
            print(f"{info}: {adyacentes_str}")

    def prim(self, nodo_inicial):
        arbol_minimo = []
        cola_prioridad = []
        visitados = set()

        # Inicializar cola de prioridad con arcos del nodo inicial
        for adyacente in self.V[nodo_inicial].adyacentes:
            heapq.heappush(cola_prioridad,
                           (self.getArco(nodo_inicial, adyacente.nombre).costo, nodo_inicial, adyacente.nombre))

        visitados.add(nodo_inicial)

        while cola_prioridad:
            costo, origen, destino = heapq.heappop(cola_prioridad)

            if destino not in visitados:
                visitados.add(destino)
                arbol_minimo.append(self.getArco(origen, destino))

                for adyacente in self.V[destino].adyacentes:
                    if adyacente.nombre not in visitados:
                        heapq.heappush(cola_prioridad,
                                       (self.getArco(destino, adyacente.nombre).costo, destino, adyacente.nombre))

        return arbol_minimo