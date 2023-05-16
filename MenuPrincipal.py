
from PyQt5 import QtCore, QtGui, QtWidgets 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("qradialgradient (spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255))")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 381, 341))
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("laberinto.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btn_pp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pp.setGeometry(QtCore.QRect(350, 480, 141, 31))
        self.btn_pp.setObjectName("btn_pp")
        self.btn_pa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pa.setGeometry(QtCore.QRect(130, 480, 141, 31))
        self.btn_pa.setObjectName("btn_pa")
        self.btn_reload = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reload.setGeometry(QtCore.QRect(130, 400, 141, 31))
        self.btn_reload.setObjectName("btn_reload")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 300, 16))
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 380, 300, 20))
        self.label_3.setObjectName("label_3")
        font_1 = QtGui.QFont()
        font_1.setPointSize(8)
        font_1.setBold(True)
        font_1.setWeight(75)
        self.label_3.setFont(font_1)
        self.tam_lab = QtWidgets.QLineEdit(self.centralwidget)
        self.tam_lab.setGeometry(QtCore.QRect(350, 410, 81, 21))
        self.tam_lab.setObjectName("tam_lab")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    #Procedimiento de inicializacion de titulos,botones,etc
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu Principal"))
        self.btn_pp.setText(_translate("MainWindow", "Primero en profundidad"))
        self.btn_pa.setText(_translate("MainWindow", "Primero en amplitud"))
        self.btn_reload.setText(_translate("MainWindow", "Regenerar Laberinto"))
        self.label_2.setText(_translate("MainWindow", "Tamaño del Laberinto: "))
        self.label_3.setText(_translate("MainWindow", "Ingrese el tamaño del laberinto"))
        self.tam_lab.setText(_translate("MainWindow", "10"))
        valor_tam_lab = self.tam_lab.text()+" X "+self.tam_lab.text()
        valor_lab_2 = self.label_2.text()
        valor_tam_lab_label_2 =valor_lab_2+""+valor_tam_lab
        self.label_2.setText((_translate("MainWindow", valor_tam_lab_label_2)))


    #Procedimiento para reimprimir y modificar el label del titulo del laberinto 
    def recargarLaberinto(self):
        valor_tam_lab = self.tam_lab.text() + " X " + self.tam_lab.text()
        valor_tam_lab_label_2 = "Tamaño del Laberinto:" + " " + valor_tam_lab
        self.label_2.setText(valor_tam_lab_label_2)
        self.label.setPixmap(QtGui.QPixmap("laberinto.png"))
        self.label.repaint()
    #Fin Procedimiento

    #Funcion para obtener  el tamaño de la matriz
    def obtenerTamMatriz(self):
        tamMatriz = self.tam_lab.text()
        return tamMatriz
    #Fin funcion