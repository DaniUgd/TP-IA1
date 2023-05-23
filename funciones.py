
import pkg_resources
import graphviz
from graphviz import Graph
from clases import nodo 
from clases import camino
import random
from colorama import init
from colorama import Fore, Back, Style
from PIL import Image
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from VentanaPP import Ventana_PP
from MenuPrincipal import Ui_MainWindow
from VentanaPA import Ventana_PA
from VentanaCompara import Ventana_Compara
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


##Funciones extraidas del archivo Gen-lab.py


#Procedimiento que imprime matriz sin grafica
def printMaze(maze,height,width):
	tam = int(height)
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				print(Fore.WHITE + str(maze[i][j]), end=" ")
			elif (maze[i][j] == '0'):
				print(Fore.GREEN + str(maze[i][j]), end=" ")
			elif(i==0 and j == 0):
				print(Fore.BLUE + str(maze[i][j]), end=" ")	
			elif(i==tam-1 and j == tam-1):
				print(Fore.BLUE + str(maze[i][j]), end=" ")	
			else:
				print(Fore.RED + str(maze[i][j]), end=" ")

		print('\n')

# Find number of surrounding cells
def surroundingCells(maze,rand_wall):
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

def gen_lab(tam):
	## Main code
	# Init variables
	wall = 'x'
	cell = '0'
	unvisited = 'u'
	height = int(tam)
	width = int(tam)
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
	starting_height = int(tam)-1
	starting_width = int(tam)-1
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
				s_cells = surroundingCells(maze,rand_wall)

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

				s_cells = surroundingCells(maze,rand_wall)
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

				s_cells = surroundingCells(maze,rand_wall)
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

				s_cells = surroundingCells(maze,rand_wall)
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
	al = random.randint(2,width-3)
	for i in range(1,al):
		maze[al][i] = cell

	maze[0][0] = salida
	maze[width-1][width-1] = entrada
	maze[0][1] = cell
	maze[width - 1][width - 2] = cell

	return maze    
#Fin Generador de matriz del laberinto

##Procedimiento para generar busqueda de camino primero en amplitud    
def primeroAmplitud(maze,flag):
	listaCamino =[]
	listaCola = []
	num_filas = int(len(maze)) - 1
	nodoI=nodo(num_filas,num_filas)
	nodoF = nodo(0,0)
	listaVisitados = set()
	listaCola.append(camino(nodoI, nodoI))
	nodoP = nodoI
	cont = 0
	while listaCola:
		listaCola=EliminaDuplicado(listaCola)
		caminoAux=listaCola.pop(0)
		nodoA=caminoAux.nodoH
		if(nodoA not in listaVisitados):

			listaVecino = []
			if(cont!=0):
				listaCamino.append(caminoAux)
			
			if nodoA == nodoF:
				if(flag==1):
					listaCaminoS=caminoSolucion(listaCamino)
					generar_arbol_jerarquico(listaCamino,listaCola,1,listaCaminoS)
					
				return listaCamino,listaCola
			
					
			listaVisitados.add(nodoA)
			listaVecino=obtenerCamino(maze,nodoA)
			
			for nodo_hijo in listaVecino:
				if(nodo_hijo not in listaVisitados):
					listaCola.append(camino(nodoA, nodo_hijo))

		cont=cont+1		
#Fin Algoritmo Primero en Amplitud

#Procedimiento para generar busqueda de camino primero en Profundidad    
def primeroProfundidad(maze,flag):
	listaCamino=[]
	listaCola=[]
	num_filas = int(len(maze)) - 1
	nodoI = nodo(num_filas,num_filas)
	nodoF = nodo(0,0)
	listaVisitados = set()
	listaCola.append(camino(nodoI, nodoI))
	cont = 0
	while listaCola:
		listaCola=EliminaDuplicado(listaCola)
		caminoAux=listaCola.pop(0)
		nodoA=caminoAux.nodoH
		
		if(nodoA not in listaVisitados):
			if(cont!=0):
				listaCamino.append(caminoAux)

			listaVisitados.add(nodoA)
			
			if nodoA == nodoF:
				
				if(flag==1):
					listaCaminoS=caminoSolucion(listaCamino)
					generar_arbol_jerarquico(listaCamino,listaCola,2,listaCaminoS)
					
				return listaCamino,listaCola
				
			listaVecino=obtenerCamino(maze,nodoA)
			pos = 0
			for nodo_hijo in listaVecino:
				if nodo_hijo not in listaVisitados:
				
					listaCola.insert(pos,camino(nodoA, nodo_hijo))
					pos=pos+1
		cont = cont+1

#Fin Algoritmo Primero en Profundidad

#Funcion para obtener caminos posibles en la matriz, la misma devuelve una lista de los posbibles
def obtenerCamino(maze,n):
	listaCamino=[]
	listaPosiciones = []
	tamM = int(len(maze))
	px=n.posX
	py=n.posY
	##Sentido Anti Horario
	if(px-1>=0 and py<tamM and py>=0):
		if maze[px-1][py]=='0' or maze[px-1][py]=='F':
			listaCamino.append(nodo(px-1,py))	
			listaPosiciones.append("ARRIBA")
	if(py-1>=0 and px<tamM and px>=0):
		if maze[px][py-1]=='0' or maze[px][py-1]=='F':
			listaCamino.append(nodo(px,py-1))
			listaPosiciones.append("IZQUIERDA")
	if(px+1<tamM and py<tamM and py>=0):
		if maze[px+1][py]=='0' or maze[px+1][py]=='F':
			listaCamino.append(nodo(px+1,py))	
			listaPosiciones.append("ABAJO")
	if(py+1<tamM and px<tamM and px>=0):
		if maze[px][py+1]=='0' or maze[px][py+1]=='F' :
			listaCamino.append(nodo(px,py+1))
			listaPosiciones.append("DERECHA")
	return listaCamino
#Fin Funcion para obtener caminos posibles

#Funcion que controla si existen nodos duplicado en listaCola
def EliminaDuplicado (listaCola):
	listaNoDuplicados = []
    # Crear un conjunto para hacer un seguimiento de los elementos ya procesados
	elementosProcesados = set()
    
    # Recorrer la lista original y agregar los elementos no duplicados a la nueva lista
	for e in listaCola:
		if e.nodoH not in elementosProcesados:
			listaNoDuplicados.append(e)
			elementosProcesados.add(e.nodoH)
    
    # Devolver la nueva lista sin elementos duplicados
	return listaNoDuplicados
#Fin Funcion

#Funcion para obtener el camino Solucion
def caminoSolucion(listaCamino):
	caminoS = []
	
	aux=nodo(0,0)
	pos=0
	for c in reversed(listaCamino):
		if((aux.posX==c.nodoH.posX and aux.posY==c.nodoH.posY)or(pos==0)):
			aux = c.nodoP
			caminoS.append(c)
			pos=1
	caminoS.reverse()

	return caminoS
	
#Fin Funcion

# Procedimiento para generar grafico del arbol
def generar_arbol_jerarquico(listacamino,listaCola,i,caminoS):
	g = Graph(engine='sfdp')
	g = graphviz.Digraph(format='png')
	h = Graph(engine='sfdp')
	h = graphviz.Digraph(format='png')
	for cam in listacamino:
		nodo_padre = (cam.nodoP.posX,cam.nodoP.posY)
		nodo_hijo = (cam.nodoH.posX,cam.nodoH.posY) 
		if(cam not in caminoS):
			g.edge(str(nodo_padre), str(nodo_hijo))
		else:
			g.node(str(nodo_padre),style="filled", fillcolor='green')
			g.node(str(nodo_hijo),style="filled", fillcolor='green')
			g.edge(str(nodo_padre),str(nodo_hijo))
	if(i<=2):
		for cam in listaCola:
			nodo_padre = (cam.nodoP.posX,cam.nodoP.posY)
			nodo_hijo = (cam.nodoH.posX,cam.nodoH.posY)
			g.node(str(nodo_hijo),style="filled", fillcolor='blue')
			g.edge(str(nodo_padre), str(nodo_hijo), style='dashed', color='blue')
	if (i==1):
		g.render('arbol_primero_amplitud')
	elif (i==2):
		g.render('arbol_primero_profundidad')
#Fin Procedimiento

def convierteNodoH(lista_camino,tam):
        listaCaminoS=caminoSolucion(lista_camino)
        listaCam = []
        listaCam.append(nodo(tam-1,tam-1))
        for c in listaCaminoS:
            listaCam.append(nodo(c.nodoH.posX,c.nodoH.posY))
        return listaCam   

def casosDePrueba():
	resultado="Estos seran los casos de prueba para los algoritmos PP y PA.\n"
	tam = 10
	ran=10
	while(tam < 51):
		resultado+="\nSe está probando con un laberinto de tamaño: " + str(tam) + "x" + str(tam) + ".\n"
		longPPC = 0
		longPAC = 0
		longPPCO = 0
		longPACO = 0
		longPPCS = 0
		longPACS = 0
		
		minlongPPC = 10000
		minlongPAC = 10000
		minlongPPCO = 10000
		minlongPACO = 10000
		minlongPPCS = 10000
		minlongPACS = 10000

		maxlongPPC = 0
		maxlongPAC = 0
		maxlongPPCO = 0
		maxlongPACO = 0
		maxlongPPCS = 0
		maxlongPACS = 0
		maze = [] 
		listaCaminoPA = []
		listaCaminoPP = []
		listaColaPA = []
		listaColaPP = []
		for i in range(0, ran):
			
			#LLamado a funciones 
			maze = gen_lab(tam)
			listaCaminoPA,listaColaPA=primeroAmplitud(maze,0)
			listaCaminoPP,listaColaPP=primeroProfundidad(maze,0)
			if (minlongPPC > len(listaCaminoPP)):
				minlongPPC = len(listaCaminoPP)
			if (minlongPAC > len(listaCaminoPA)):
				minlongPAC = len(listaCaminoPA)	
			if (minlongPPCO > len(listaColaPP)):
				minlongPPCO = len(listaColaPP)	
			if (minlongPACO > len(listaColaPA)):
				minlongPACO = len(listaColaPA)
			if (minlongPPCS > len(convierteNodoH(listaCaminoPP,tam))):
				minlongPPCS = len(convierteNodoH(listaCaminoPP,tam))	
			if (minlongPACS > len(convierteNodoH(listaCaminoPA,tam))):
				minlongPACS = len(convierteNodoH(listaCaminoPA,tam))
				
			if (maxlongPPC < len(listaCaminoPP)):
				maxlongPPC = len(listaCaminoPP)
			if (maxlongPAC < len(listaCaminoPA)):
				maxlongPAC = len(listaCaminoPA)	
			if (maxlongPPCO < len(listaColaPP)):
				maxlongPPCO = len(listaColaPP)	
			if (maxlongPACO < len(listaColaPA)):
				maxlongPACO = len(listaColaPA)
			if (maxlongPPCS < len(convierteNodoH(listaCaminoPP,tam))):
				maxlongPPCS = len(convierteNodoH(listaCaminoPP,tam))	
			if (maxlongPACS < len(convierteNodoH(listaCaminoPA,tam))):
				maxlongPACS = len(convierteNodoH(listaCaminoPA,tam))

			longPPC = longPPC + len(listaCaminoPP)
			longPAC = longPAC + len(listaCaminoPA)
			longPPCO = longPPCO + len(listaColaPP)
			longPACO = longPACO + len(listaColaPA)
			longPPCS = longPPCS + len(convierteNodoH(listaCaminoPP,tam))
			longPACS = longPACS + len(convierteNodoH(listaCaminoPA,tam))
		resultado +="Cant Prom Nodos Totales PP.\n"
		resultado +="Prom:"+str(longPPC/ran)+"\t min:"+str(minlongPPC)+"\t max:"+str(maxlongPPC)+"\n"
		resultado +="Cant Prom Nodos Totales PA.\n"
		resultado +="Prom:"+str(longPAC/ran)+"\t min:"+str(minlongPAC)+"\t max:"+str(maxlongPAC)+"\n"
		resultado +="Cant Prom Nodos en Cola PP.\n"
		resultado +="Prom:"+str(longPPCO/ran)+"\t min:"+str(minlongPPCO)+"\t max:"+str(maxlongPPCO)+"\n"
		resultado +="Cant Prom Nodos en Cola PA.\n"
		resultado +="Prom:"+str(longPACO/ran)+"\t min:"+str(minlongPACO)+"\t max:"+str(maxlongPACO)+"\n"
		resultado +="Cant Prom Nodos Camino Sol PP.\n"
		resultado +="Prom:"+str(longPPCS/ran)+"\t min:"+str(minlongPPCS)+"\t max:"+str(maxlongPPCS)+"\n"
		resultado +="Cant Prom Nodos Camino Sol PA.\n"
		resultado +="Prom:"+str(longPACS/ran)+"\t min:"+str(minlongPACS)+"\t max:"+str(maxlongPACS)+"\n"
		tam=tam+10
	archivo = open("casos.txt", "w")	
	archivo.write(resultado)
	archivo.close()
	QMessageBox.information(None, "Mensaje", "Se ejecutaron correctamente los casos de prueba. Los casos se guardaron en el archivo 'casos.txt' ubicado en la misma carpeta que el ejecutable.")


#Procedimiento para generar la imagen de laberinto
def generarLab(laberinto,listaCamino,i):
    
    # Abrir imágenes
	
    pared = Image.open(pkg_resources.resource_filename(__name__, 'pared.png'))
    camino = Image.open(pkg_resources.resource_filename(__name__, 'camino.png'))
    caminoSol = Image.open(pkg_resources.resource_filename(__name__, 'caminoSol.png'))
    # Tamaño de la imagen
    tam = len(laberinto)
    imagen = Image.new("RGB", (tam*50, tam*50), "white")
    listaCam=[]
    if (listaCamino is not None):
        listaCam = convierteNodoH(listaCamino,tam)
    # Pegar imágenes
    for fila in range(tam):
        for columna in range(tam):
            if (laberinto[fila][columna] == '0' or laberinto[fila][columna] == 'I' or laberinto[fila][columna] == 'F') and (listaCamino is None or nodo(fila,columna) not in listaCam):
                img = camino
            elif laberinto[fila][columna] == 'x':
                img = pared
            elif listaCamino is not None and nodo(fila,columna) in listaCam:
                img = caminoSol
            else:
                continue
            img = img.resize((50, 50), Image.ANTIALIAS)
            imagen.paste(img, (columna*50, fila*50))

    if(i == 0):
 		# Guardar imagen
        imagen.save("laberinto.png")
    if(i == 1):
		# Guardar imagen laberinto algoritmo pp
        imagen.save("laberintoPP.png")
    elif(i == 2):
		# Guardar imagen laberinto algoritmo pa
        imagen.save("laberintoPA.png")	


#Fin Procedimiento


#Clases y funciones de intefaz
class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_pp.clicked.connect(self.abrirNuevaVentanaPP)
        self.ui.btn_pa.clicked.connect(self.abrirNuevaVentanaPA)
        self.ui.btn_compara.clicked.connect(self.abrirNuevaVentanaCompara)
        self.ui.btn_reload.clicked.connect(self.regenerarLaberinto)
        self.ui.btn_prueba.clicked.connect(self.abrirNuevaVentanaPruebas)
        validator = QRegExpValidator(QRegExp("^(?:[5-9]|[1-9][0-9])$"), self.ui.tam_lab)
        self.ui.tam_lab.setValidator(validator)
    ##Procedimiento para Recargar el laberinto y sus algoritmos
    def regenerarLaberinto(self):
        tam = self.ui.obtenerTamMatriz()
        fila = int(tam)
        if(fila > 4 and fila <51 ):
            global maze, listaCaminoPA, listaCaminoPP  # Agregar "global" para modificar las variables globales
            maze = []
            listaCaminoPA = []
            listaCaminoPP = []
            listaColaPA = []
            listaColaPP = []
			#LLamado a funciones 
            maze = gen_lab(fila)
            listaCaminoPA,listaColaPA=primeroAmplitud(maze,1)
            listaCaminoPP,listaColaPP=primeroProfundidad(maze,1)
            generarLab(maze,None,0)
            generarLab(maze,listaCaminoPA,2)
            generarLab(maze,listaCaminoPP,1)
            self.ui.recargarLaberinto()
        else:
            QMessageBox.information(None, "Mensaje", "Solo se acepta numeros entre el 5 y el 50.")
       #Fin Procedimiento

    #Procedimiento Para el funcionamiento de los botones    
    def abrirNuevaVentanaPP(self):
        self.ventana_pp = VentanaPP()
        self.ventana_pp.show()

    def abrirNuevaVentanaPA(self):
        self.ventana_pp = VentanaPA()
        self.ventana_pp.show()

    def abrirNuevaVentanaCompara(self):
        self.ventana_compara = VentanaCompara()
        self.ventana_compara.show()

    def abrirNuevaVentanaPruebas(self):
        casosDePrueba()			
    #Fin procedimiento

#Clases Para el funcionamiento de las interfaces    
class VentanaPP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ventana_PP()
        self.ui.setupUi(self, listaCaminoPP)

class VentanaPA(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ventana_PA()
        self.ui.setupUi(self, listaCaminoPA)

class VentanaCompara(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ventana_Compara()
        self.ui.setupUi(self)
#Fin De las clases


def devuelveMov(caminoMov):
	if(caminoMov.nodoP.posX < caminoMov.nodoH.posX ):
		return "Abajo"
	if(caminoMov.nodoP.posY > caminoMov.nodoH.posY ):
		return "Izquierda"
	if(caminoMov.nodoP.posX > caminoMov.nodoH.posX ):
		return "Arriba"
	if(caminoMov.nodoP.posY < caminoMov.nodoH.posY ):
		return "Derecha"
	

