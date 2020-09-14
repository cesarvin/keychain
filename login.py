# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from menu import Ui_Menu
from keychain import *


class Ui_Login(object):
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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 210, 301, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit_passwordMaster = QtWidgets.QTextEdit(self.frame)
        self.textEdit_passwordMaster.setGeometry(QtCore.QRect(90, 250, 301, 31))
        self.textEdit_passwordMaster.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_passwordMaster.setObjectName("textEdit_passwordMaster")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 301, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Proyecto1/keychain/logo.jpeg"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_ingresar = QtWidgets.QPushButton(self.frame)
        self.pushButton_ingresar.setGeometry(QtCore.QRect(180, 300, 113, 32))
        self.pushButton_ingresar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.pushButton_ingresar.setObjectName("pushButton_ingresar")
        self.pushButton_ingresar.clicked.connect(self.ingresar_sitio)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ingrese contraseña maestra"))
        self.pushButton_ingresar.setText(_translate("MainWindow", "Ingresar"))

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

    def ingresar_sitio(self):
        k = Keychain()
        password = self.textEdit_passwordMaster.toPlainText()
        k.init(password)
        
        # carga los datos 
        tuples, tuples_password = k.dump()

        # verifica la contraseña y la integridad de 
        isload = k.load(password, None, None)

        if isload == False:
            k = None
            self.openPopUpError("Contraseña incorrecta")

        # si isload = true se ejecutan las opciones del programa, sino se vuelve a solicitar la clave maestra.
        else:
            self.openPopUpSucces("Contraseña correcta")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Menu(password)
            self.ui.setupUi(self.window)
            Login.hide()
            self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())


