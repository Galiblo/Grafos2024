class Arco:
    def __init__(self, origen, destino, costo):
        """

        :param origen: Nodo de origen
        :param destino: Nodo de destino
        :param costo: Costo del arco
        """
        self.origen = origen
        self.destino = destino
        self.costo = costo

    def __str__(self):
        return self.origen.nombre + " - " + self.destino.nombre + " : " + str(self.costo)