# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from keychain import *


class Ui_Search(object):
    def __init__(self, password):
        super(Ui_Search, self).__init__()
        self.password = password

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(248, 139, 149);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(190, 80, 471, 401))
        self.frame.setStyleSheet("background-color: rgb(255, 245, 222);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit_site = QtWidgets.QTextEdit(self.frame)
        self.textEdit_site.setGeometry(QtCore.QRect(90, 170, 301, 31))
        self.textEdit_site.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_site.setObjectName("textEdit_site")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(90, 130, 301, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 301, 121))
        self.label_4.setStyleSheet("font: 16pt \".SF NS Text\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        # self.tableWidget = QtWidgets.QTableWidget(self.frame)
        # self.tableWidget.setGeometry(QtCore.QRect(90, 300, 301, 53))
        # self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        # self.tableWidget.setWordWrap(True)
        # self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(2)
        # self.tableWidget.setRowCount(0)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_buscar = QtWidgets.QPushButton(self.frame)
        self.pushButton_buscar.setGeometry(QtCore.QRect(190, 230, 113, 32))
        self.pushButton_buscar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.pushButton_buscar.setObjectName("pushButton_buscar")
        self.pushButton_buscar.clicked.connect(self.buscar_sitio)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Ingrese sitio"))
        self.label_4.setText(_translate("MainWindow", "BUSCAR"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("MainWindow", "SITIO"))
        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("MainWindow", "PASSWORD"))
        self.pushButton_buscar.setText(_translate("MainWindow", "Buscar"))

    def openPopUpError(self, mensaje):
        msgError = QMessageBox()
        msgError.setText(mensaje)
        msgError.setIcon(QMessageBox.Warning)
        x = msgError.exec_()

    def openPopUpSucces(self, mensaje):
        msgError = QMessageBox()
        msgError.setText(mensaje)
        msgError.setIcon(QMessageBox.Information)
        x = msgError.exec_()

    def buscar_sitio(self):
        k = Keychain()
        k.init(self.password)
    
        # carga los datos 
        tuples, tuples_password = k.dump()

        # verifica la contraseña y la integridad de 
        isload = k.load(self.password, None, None)

        if isload == False:
            k = None
            self.openPopUpError("error en programa")

        # si isload = true se ejecutan las opciones del programa, sino se vuelve a solicitar la clave maestra.
        else:
            sitio = self.textEdit_site.toPlainText()
            contraseña_sitio = k.get_value(sitio)
            if contraseña_sitio == None:
                self.openPopUpError("El sitio no existe")
            else:
                self.openPopUpSucces(contraseña_sitio)
            

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Search = QtWidgets.QMainWindow()
#     ui = Ui_Search()
#     ui.setupUi(Search)
#     Search.show()
#     sys.exit(app.exec_())


