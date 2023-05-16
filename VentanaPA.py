
from PyQt5 import QtCore, QtGui, QtWidgets


class Ventana_PA(object):
    def setupUi(self, Form,listaCamino):
        Form.setObjectName("Form")
        Form.resize(830, 600)
        Form.setAccessibleName("")
        Form.setStyleSheet("")
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 50, 651, 541))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(-189, 0, 821, 3725))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("arbol_primero_amplitud.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.titulo_imagen = QtWidgets.QLabel(Form)
        self.titulo_imagen.setGeometry(QtCore.QRect(10, 10, 651, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titulo_imagen.setFont(font)
        self.titulo_imagen.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_imagen.setObjectName("titulo_imagen")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(680, -5, 121, 61))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        ## Propiedades de la tabla_Camino
        self.tabla_Camino = QtWidgets.QTableWidget(Form)
        self.tabla_Camino.setGeometry(QtCore.QRect(670, 50, 145, 541))
        self.tabla_Camino.setColumnCount(2)
        self.tabla_Camino.setObjectName("tabla_Camino")
        item = QtWidgets.QTableWidgetItem()
        self.tabla_Camino.setVerticalHeaderItem(0, item)
        self.tabla_Camino.horizontalHeader().setDefaultSectionSize(50)
        self.tabla_Camino.horizontalHeader().setMinimumSectionSize(39)
        longCamino = len(listaCamino)
        self.tabla_Camino.setRowCount(longCamino)
        
        # Agregar los valores de la lista a la tabla
        cont = 0
        for i in listaCamino:
            item1 = QtWidgets.QTableWidgetItem(str(i.nodoP.posX) + " , " + str(i.nodoP.posY))
            item2 = QtWidgets.QTableWidgetItem(str(i.nodoH.posX) + " , " + str(i.nodoH.posY))
            self.tabla_Camino.setItem(cont, 0, item1)
            self.tabla_Camino.setItem(cont, 1, item2)
            cont=cont+1
            
        # Crear objetos QTableWidgetItem para los encabezados
        header1 = QtWidgets.QTableWidgetItem("Padre")
        header2 = QtWidgets.QTableWidgetItem("Hijo")

        # Establecer los encabezados en la tabla
        self.tabla_Camino.setHorizontalHeaderItem(0, header1)
        self.tabla_Camino.setHorizontalHeaderItem(1, header2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        


    #Procedimiento de inicializacion de titulos,botones,etc
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AlgoritmoPA"))
        self.titulo_imagen.setText(_translate("Form", "Gráfico del Algoritmo Primero en Amplitud"))
        self.label.setText(_translate("Form", "Tabla de Pasos"))


