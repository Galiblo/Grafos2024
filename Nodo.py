class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.adyacentes = []
        self.d = float("Inf")
        self.f = 0
        self.color = None
        self.padre = None
        self.id = 0

    def addAdyacente(self,destino):
        if destino not in self.adyacentes:
            self.adyacentes.append(destino)

    def __str__(self):
        adyacentes = []
        for nodo in self.adyacentes:
            adyacentes.append(nodo.nombre)
        if len(adyacentes) > 0:
            adyacentes = ", ".join(adyacentes)
        else:
            adyacentes = ""
        if self.padre is None:
            padre = ""
        else:
            padre = self.padre.nombre
        return f"{self.nombre}, d({self.d}), f({self.f}), p({padre}), {self.color}, id({self.id}): {adyacentes}"