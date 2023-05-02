import funciones
from clases import nodo 
maze = [] 
nodoI = nodo(9, 9)
nodoF = nodo(0, 0)
listaCamino = []
listaVisitados = set()


# Print final maze
maze = funciones.gen_lab()

funciones.printMaze(maze,10,10)
funciones.primeroAmplitud(maze)
##funciones.primeroProfundidad(maze)
##funciones.primeroProfundidadRecursivo(maze, nodoI, nodoF, listaVisitados, listaCamino)

