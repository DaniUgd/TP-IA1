from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw
    
    
class Ventana_PA(object):
    def setupUi(self, Form,listaCamino):
        Form.setObjectName("Form")
        Form.resize(636, 591)
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(60, 20, 300, 300))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 426, 1805))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("arbol_primero_amplitud.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(60, 340, 301, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        longCamino = len(listaCamino)
        self.tableWidget.setRowCount(longCamino)

        
        # Agregar los valores de la lista a la tabla
        cont = 0
        for i in listaCamino:
            item1 = QtWidgets.QTableWidgetItem(str(i.nodoP.posX) + " , " + str(i.nodoP.posY))
            item2 = QtWidgets.QTableWidgetItem(str(i.nodoH.posX) + " , " + str(i.nodoH.posY))
            self.tableWidget.setItem(cont, 0, item1)
            self.tableWidget.setItem(cont, 1, item2)
            cont=cont+1
            
        # Crear objetos QTableWidgetItem para los encabezados
        header1 = QtWidgets.QTableWidgetItem("Padre")
        header2 = QtWidgets.QTableWidgetItem("Hijo")

        # Establecer los encabezados en la tabla
        self.tableWidget.setHorizontalHeaderItem(0, header1)
        self.tableWidget.setHorizontalHeaderItem(1, header2)

        
        QtCore.QMetaObject.connectSlotsByName(Form)

   
