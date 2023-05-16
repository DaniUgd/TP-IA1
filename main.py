import sys
import funciones
from clases import nodo 
from PyQt5.QtWidgets import QApplication
from funciones import MenuPrincipal

#Inicializacion de las variables Globales
maze = [] 
nodoI = nodo(9, 9)
nodoF = nodo(0, 0)
listaCaminoPA = []
listaCaminoPP = []
listaVisitados = set()

#LLamado a funciones 
maze = funciones.gen_lab(10)
funciones.primeroAmplitud(maze,listaCaminoPA)
funciones.primeroProfundidad(maze,listaCaminoPP)
funciones.generarLab(maze)

#Ejecucion de aplicacion (menu principal)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MenuPrincipal()
    ventana.show()
    sys.exit(app.exec_())
