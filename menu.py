# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from delete import Ui_Delete
from insert import Ui_Insert
from search import Ui_Search

class Ui_Menu(object):
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
        self.pushButton_insertar = QtWidgets.QPushButton(self.frame)
        self.pushButton_insertar.setGeometry(QtCore.QRect(180, 60, 113, 32))
        self.pushButton_insertar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.pushButton_insertar.setObjectName("pushButton_insertar")
        self.pushButton_buscar = QtWidgets.QPushButton(self.frame)
        self.pushButton_buscar.setGeometry(QtCore.QRect(180, 140, 113, 32))
        self.pushButton_buscar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.pushButton_buscar.setObjectName("pushButton_buscar")
        self.pushButton_eliminar = QtWidgets.QPushButton(self.frame)
        self.pushButton_eliminar.setGeometry(QtCore.QRect(180, 220, 113, 32))
        self.pushButton_eliminar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")
        self.pushButton_salir = QtWidgets.QPushButton(self.frame)
        self.pushButton_salir.setGeometry(QtCore.QRect(180, 300, 113, 32))
        self.pushButton_salir.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.pushButton_salir.setObjectName("pushButton_salir")
        self.pushButton_eliminar.clicked.connect(self.openDelete)
        self.pushButton_insertar.clicked.connect(self.openInsert)
        self.pushButton_buscar.clicked.connect(self.openSearch)
        self.pushButton_salir.clicked.connect(QtCore.QCoreApplication.instance().quit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_insertar.setText(_translate("MainWindow", "Insertar"))
        self.pushButton_buscar.setText(_translate("MainWindow", "Buscar"))
        self.pushButton_eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.pushButton_salir.setText(_translate("MainWindow", "Salir"))

    def openDelete(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Delete()
        self.ui.setupUi(self.window)
        self.window.show()

    def openInsert(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Insert()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSearch(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Search()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())

