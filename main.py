import funciones
from clases import nodo 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from inter2 import Ui_MainWindow

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # Crear una instancia de la interfaz de usuario
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
maze = [] 
nodoI = nodo(9, 9)
nodoF = nodo(0, 0)
listaCamino = []
listaVisitados = set()


# Print final maze
maze = funciones.gen_lab()

funciones.printMaze(maze,10,10)
funciones.primeroAmplitud(maze)
funciones.primeroProfundidad(maze)
##funciones.primeroProfundidadRecursivo(maze, nodoI, nodoF, listaVisitados, listaCamino)

