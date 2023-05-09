import funciones
from clases import nodo 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from VentanaPP import Ventana_PP
from MenuPrincipal import VentanaMenuPrincipal

maze = [] 
nodoI = nodo(9, 9)
nodoF = nodo(0, 0)
listaCamino = []
listaVisitados = set()


# Print final maze
maze = funciones.gen_lab()

funciones.printMaze(maze,10,10)
funciones.primeroAmplitud(maze,listaCamino)
funciones.primeroProfundidad(maze)
##funciones.primeroProfundidadRecursivo(maze, nodoI, nodoF, listaVisitados, listaCamino)

funciones.generarLab(maze)

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # Crear una instancia de la interfaz de usuario
        self.ui = VentanaMenuPrincipal()
        self.ui.setupUi(self)
        self.ui.btn_pp.clicked.connect(self.abrirNuevaVentana)
    
    def abrirNuevaVentana(self):
        
        self.Ventana_P = VentanaPP()
        self.Ventana_P.show()
        
        
class VentanaPP(QMainWindow):
    def __init__(self):
        super().__init__()
        # Crear una instancia de la interfaz de usuario
        self.ui = Ventana_PP()
        self.ui.setupUi(self,listaCamino)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MenuPrincipal()
    ventana.show()
    sys.exit(app.exec_())


