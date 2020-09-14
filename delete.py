# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Delete(object):
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
        self.textEdit_site.setGeometry(QtCore.QRect(90, 210, 301, 31))
        self.textEdit_site.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_site.setObjectName("textEdit_site")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 301, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 301, 121))
        self.label_4.setStyleSheet("font: 16pt \".SF NS Text\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_eliminar = QtWidgets.QPushButton(self.frame)
        self.pushButton_eliminar.setGeometry(QtCore.QRect(180, 270, 113, 32))
        self.pushButton_eliminar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")
        self.pushButton_eliminar.clicked.connect(self.prueba)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Ingrese sitio"))
        self.label_4.setText(_translate("MainWindow", "ELIMINAR"))
        self.pushButton_eliminar.setText(_translate("MainWindow", "Eliminar"))

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

    def prueba(self):
        print("Si funciona al presionar")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Delete = QtWidgets.QMainWindow()
    ui = Ui_Delete()
    ui.setupUi(Delete)
    Delete.show()
    sys.exit(app.exec_())

