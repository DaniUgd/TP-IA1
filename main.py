import funciones
from clases import nodo 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from VentanaPP import Ventana_PP
from MenuPrincipal import VentanaMenuPrincipal
from VentanaPA import Ventana_PA
maze = [] 
nodoI = nodo(9, 9)
nodoF = nodo(0, 0)
listaCaminoPA = []
listaCaminoPP = []

listaVisitados = set()


# Print final maze
maze = funciones.gen_lab()

funciones.printMaze(maze,10,10)
funciones.primeroAmplitud(maze,listaCaminoPA)
funciones.primeroProfundidad(maze,listaCaminoPP)


funciones.generarLab(maze)

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # Crear una instancia de la interfaz de usuario
        self.ui = VentanaMenuPrincipal()
        self.ui.setupUi(self)
        self.ui.btn_pp.clicked.connect(self.abrirNuevaVentanaPP)
        self.ui.btn_pa.clicked.connect(self.abrirNuevaVentanaPA)
    
    def abrirNuevaVentanaPP(self):
        
        self.Ventana_PP = VentanaPP()
        self.Ventana_PP.show()

    def abrirNuevaVentanaPA(self):
        self.Ventana_PA = VentanaPA()
        self.Ventana_PA.show()        
        
class VentanaPP(QMainWindow):
    def __init__(self):
        super().__init__()
        # Crear una instancia de la interfaz de usuario
        self.ui = Ventana_PP()
        self.ui.setupUi(self,listaCaminoPP)

class VentanaPA(QMainWindow):
    def __init__(self):
        super().__init__()
        # Crear una instancia de la interfaz de usuario
        self.ui = Ventana_PA()
        self.ui.setupUi(self,listaCaminoPA)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MenuPrincipal()
    ventana.show()
    sys.exit(app.exec_())


