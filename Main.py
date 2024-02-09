from Grafo import Grafo
from Nodo import Nodo
from Arco import Arco

archivo = open("prim2.txt")
lineas = archivo.readlines()
error = 1
G = Grafo("Grafo")

for error, linea in enumerate(lineas):
    linea = linea.rstrip()
    linea = linea.lower()
    renglon = linea.split()
    if len(renglon) ==2 or len(renglon) > 3:
        print(f"Error de sintaxis en el renglon {error+1}, ({linea})")
        exit(1)
    elif len(renglon) == 3:
        G.addNodo(renglon[0])
        G.addNodo(renglon[1])
        G.addArco(renglon[0], renglon[1], renglon[2])
    elif len(renglon) == 1:
        G.addNodo(renglon[0])

print("Grafo original")
G.DFS()
print(G)

print("Grafo Kruskal")
arbol_minimo = G.kruskal()
G.imprimir_arbol_minimo(arbol_minimo)
print()

print("Grafo Prim")
nodo_inicial = "s"  # inicio del algoritmo prim
arbol_minimo = G.prim(nodo_inicial)
G.imprimir_arbol_minimo(arbol_minimo)