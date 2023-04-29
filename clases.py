class nodo :

    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY
    ##funciones para comparar dos objetos de la misma clase
    def __eq__(self, other):
        if isinstance(other, nodo):
            return self.posX == other.posX and self.posY == other.posY
        return False

    def __hash__(self):
        return hash((self.posX, self.posY))
    def __str__(self):
        return f"({self.posX}, {self.posY})"
    def imprimir_nodos(self):
        for nodo in self.lista_de_nodos:
            print(nodo.__str__())
 
class camino : 

    def __init__(self, nodoP,nodoH):
        self.nodoP = nodoP
        self.nodoH = nodoH
        

