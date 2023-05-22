import sys
import funciones
from clases import nodo 
from PyQt5.QtWidgets import QApplication
from funciones import MenuPrincipal

#Inicializacion de las variables Globales
maze = [] 
listaCaminoPA = []
listaCaminoPP = []
listaColaPA = []
listaColaPP = []
#LLamado a funciones 
maze = funciones.gen_lab(10)
listaCaminoPA,listaColaPA=funciones.primeroAmplitud(maze,1)
listaCaminoPP,listaColaPP = funciones.primeroProfundidad(maze,1)
funciones.generarLab(maze,None,0)
funciones.generarLab(maze,listaCaminoPP,1)
funciones.generarLab(maze,listaCaminoPA,2)
#funciones.casosDePrueba()
#Ejecucion de aplicacion (menu principal)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MenuPrincipal()
    ventana.show()
    funciones.MenuPrincipal().regenerarLaberinto()
    sys.exit(app.exec_())
