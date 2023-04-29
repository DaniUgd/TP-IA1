import funciones
from clases import nodo 
maze = [] 
nodoI = nodo(9, 9)
nodoF = nodo(0, 0)
listaCamino = []
listaVisitados = set()


# Print final maze
maze = funciones.gen_lab()
tiempoProfundidad = 0;
tiempoAmplitud = 0;
funciones.printMaze(maze,10,10)
funciones.primeroAmplitud(maze,tiempoAmplitud)
funciones.primeroProfundidad(maze)
##funciones.primeroProfundidadRecursivo(maze, nodoI, nodoF, listaVisitados, listaCamino)

