# Maze generator -- Randomized Prim Algorithm

## Imports

import matplotlib.pyplot as plt
from PIL import Image
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import graphviz
from clases import nodo 
from clases import camino
import random
import time
import numpy as np
from colorama import init
from colorama import Fore, Back, Style





## izquierda:-1 ,derecha: +1, arriba: -1,abajo +1
## Functions


def generar_arbol_jerarquico(listacamino):
    g = graphviz.Digraph(format='png')
    nodos_visitados = set()
    for camino in listacamino:
        nodo_padre = (camino.nodoP.posX,camino.nodoP.posY)
        nodo_hijo = camino.nodoH.posX,camino.nodoH.posY
        if nodo_padre not in nodos_visitados:
            g.node(str(nodo_padre))
            nodos_visitados.add(nodo_padre)
        if nodo_hijo not in nodos_visitados:
            g.node(str(nodo_hijo))
            nodos_visitados.add(nodo_hijo)
        g.edge(str(nodo_padre), str(nodo_hijo))
    g.render('arbol_primero_anchura')
    
   

# Luego de generar la lista de camino con primeroAnchura(maze)...


    
def primeroAnchura(maze):
	
	nodoI=nodo(9,9)
	nodoF = nodo(0,0)
	listaCamino=[]
	listaVisitados = set()
	listaCola = []
	listaCola.append(nodoI)
	 
	while listaCola:
		nodoA=listaCola.pop(0)
		if(nodoA not in listaVisitados):
			listaVecino = []
			listaVisitados.add(nodoA)
			listaVecino=obtenerCamino(maze,nodoA)
			for e in listaVecino:
				if(e not in listaVisitados):
					listaCola.append(e)
					nodoAux=camino(nodoA,e)
					listaCamino.append(nodoAux)
		
		# Crear un grafo vacío
	
	generar_arbol_jerarquico(listaCamino)



		

	

	

def obtenerCamino(maze,n):
	listaCamino=[]
	px=n.posX
	py=n.posY
	
	if(py+1<10 and px<10 and px>=0):
		if maze[px][py+1]=='0' or maze[px][py+1]=='F' :
			listaCamino.append(nodo(px,py+1))
			
	if(py-1>=0 and px<10 and px>=0):
		if maze[px][py-1]=='0' or maze[px][py-1]=='F':
			listaCamino.append(nodo(px,py-1))

	if(px-1>=0 and py<10 and py>=0):
		if maze[px-1][py]=='0' or maze[px-1][py]=='F':
			listaCamino.append(nodo(px-1,py))

	if(px+1<10 and py<10 and py>=0):
		if maze[px+1][py]=='0' or maze[px+1][py]=='F':
			listaCamino.append(nodo(px+1,py))
			
	return listaCamino


"""
def obtenerCamino(maze,n):
	listaCamino=[]
	px=n.posX
	py=n.posY
	print("aca esta la px",px)
	print('inicio',px,py)
	if(px+1<10 and py<10 and py>=0):
		if maze[px+1][py]=='0':
			guardarPos(px,py,px+1,py,listaCamino)
			print('abajo',px+1,py)

	if(px-1>0 and py<10 and py>=0):
		if maze[px-1][py]=='0':
			guardarPos(px,py,px-1,py,listaCamino)
			print('arriba',px-1,py)

	if(py+1<10 and px<10 and px>=0):
		if maze[px][py+1]=='0':
			guardarPos(px,py,px,py+1,listaCamino)
			print('der',px,py+1)
			
	if(py-1>=0 and px<10 and px>=0):
		if maze[px][py-1]=='0':
			guardarPos(px,py,px,py-1,listaCamino)
			print('izq',px,py-1)
	return listaCamino
		
def guardarPos(pospX,pospY,poshX,poshY,listaCamino):
	posicionP = nodo(pospX, pospY)
	posicionH = nodo(poshX, poshY)
	nodoP = camino(posicionP,posicionH)
	listaCamino.append(nodoP)
"""



def buscar_posiciones(maze,i,j):
	posiciones = []

	if (maze[i][j-1]=='0' ):
			posiciones.append('izq')
			
	if (j<9 and maze[i][j+1]=='0' ):
			posiciones.append('der')
	
	if (maze[i-1][j]=='0'  ):
			posiciones.append('arr')
	if (i<9 and maze[i+1][j]=='0' ):
			posiciones.append('abj')
	return posiciones



def printMaze(maze):
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				print(Fore.WHITE + str(maze[i][j]), end=" ")
			elif (maze[i][j] == '0'):
				print(Fore.GREEN + str(maze[i][j]), end=" ")
			elif(i==0 and j == 0):
				print(Fore.BLUE + str(maze[i][j]), end=" ")	
			elif(i==9 and j == 9):
				print(Fore.BLUE + str(maze[i][j]), end=" ")	
			else:
				print(Fore.RED + str(maze[i][j]), end=" ")

		print('\n')

# Find number of surrounding cells
def surroundingCells(rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == '0'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == '0'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == '0'):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == '0'):
		s_cells += 1

	return s_cells


## Main code
# Init variables
wall = 'x'
cell = '0'
unvisited = 'u'
height = 10
width = 10
maze = []
entrada = 'I'
salida = 'F'

# Initialize colorama
init()

# Denote all cells as unvisited
for i in range(0, height):
	line = []
	for j in range(0, width):
		line.append(unvisited)
	maze.append(line)

# Randomize starting point and set it a cell
starting_height = int(9)
starting_width = int(9)
if (starting_height == 0):
	starting_height += 1
if (starting_height == height-1):
	starting_height -= 1
if (starting_width == 0):
	starting_width += 1
if (starting_width == width-1):
	starting_width -= 1

# Mark it as cell and add surrounding walls to the list
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

# Denote walls in maze
maze[starting_height-1][starting_width] = 'x'
maze[starting_height][starting_width - 1] = 'x'
maze[starting_height][starting_width + 1] = 'x'
maze[starting_height + 1][starting_width] = 'x'

while (walls):
	# Pick a random wall
	rand_wall = walls[int(random.random()*len(walls))-1]

	# Check if it is a left wall
	if (rand_wall[1] != 0):
		if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == '0'):
			# Find the number of surrounding cells
			s_cells = surroundingCells(rand_wall)

			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = '0'

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'x'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])


				# Bottom cell
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'x'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):	
					if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'x'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
			

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check if it is an upper wall
	if (rand_wall[0] != 0):
		if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == '0'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = '0'

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'x'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'x'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])

				# Rightmost cell
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'x'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check the bottom wall
	if (rand_wall[0] != height-1):
		if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == '0'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = '0'

				# Mark the new walls
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'x'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'x'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'x'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)


			continue

	# Check the right wall
	if (rand_wall[1] != width-1):
		if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == '0'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = '0'

				# Mark the new walls
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'x'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'x'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[0] != 0):	
					if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'x'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Delete the wall from the list anyway
	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
	


# Mark the remaining unvisited cells as walls
for i in range(0, height):
	for j in range(0, width):
		if (maze[i][j] == 'u'):
			maze[i][j] = 'x'

# Set entrance and exit
for i in range(0, width):
	if (maze[1][i] == '0'):
		maze[0][i] = '0'
		break

for i in range(width-1, 0, -1):
	if (maze[height-2][i] == '0'):
		maze[height-1][i] = '0'
		break
al = random.randint(2,7)
for i in range(1,al):
	maze[al][i] = cell

maze[0][0] = salida
maze[9][9] = entrada
maze[0][1] = cell
maze[9][8] = cell

# Print final maze
printMaze(maze)

primeroAnchura(maze)



## izquierda:-1 ,derecha: +1, arriba: -1,abajo +1





			
"""
	while (i>0):
		while (j>0):
			if(maze[i][j]=='0' or maze[i][j]== 'F' or maze[i][j]== 'I'):
				
				print(i,j)
				posicion = (buscar_posiciones(maze,i,j)) 
				print(posicion)
				if([i,j] in grafo):

					i=i+1
					break
				else:
					if('arr' in posicion ):
						i=i-1
						camino.append([i,j])
					
					else:
						if('izq' in posicion):
							j=j-1
							camino.append([i,j])
							break
						if('der' in posicion):
							j=j+1
							camino.append([i,j])
							break
						if('abj' in posicion):
							grafo=camino
							print("la concha de tu madre")
							print(grafo)
							i=i+1
							break
						
			else:
				j=j-1			
"""




