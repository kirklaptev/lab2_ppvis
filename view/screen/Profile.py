# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel, QWidget)


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Profile(QMainWindow, object):
    def __init__(self, c, m):
        super().__init__()
        self.model = m
        self.controller = c
        Profile = QWidget()

        self.setObjectName("Profile")
        self.resize(300, 400)
        self.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(Profile)
        self.centralwidget.setObjectName("centralwidget")
        self.text_name = QtWidgets.QLabel(self.centralwidget)
        self.text_name.setGeometry(QtCore.QRect(0, 30, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.text_name.setFont(font)
        self.text_name.setStyleSheet("color: rgb(156, 156, 255);")
        self.text_name.setObjectName("text_name")

        self.btn_create_recipe = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create_recipe.setGeometry(QtCore.QRect(50, 110, 180, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_create_recipe.setFont(font)
        self.btn_create_recipe.setStyleSheet("background-color: rgb(138, 138, 138);\n"
"color: rgb(255, 255, 255);")
        self.btn_create_recipe.setObjectName("btn_create_recipe")

        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.btn_exit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(156, 156, 156);")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.clicked.connect(lambda: self.controller.showFirst())#showFirst

        self.btn_settings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_settings.setGeometry(QtCore.QRect(150, 0, 150, 30))
        self.btn_settings.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(156, 156, 156);")
        self.btn_settings.setObjectName("btn_settings")
        self.btn_settings.clicked.connect(lambda: self.controller.showSettings())#showSettings

        self.btn_favorite_recipes = QtWidgets.QPushButton(self.centralwidget)
        self.btn_favorite_recipes.setGeometry(QtCore.QRect(50, 180, 180, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_favorite_recipes.setFont(font)
        self.btn_favorite_recipes.setStyleSheet("background-color: rgb(138, 138, 138);\n"
"color: rgb(255, 255, 255);")
        self.btn_favorite_recipes.setObjectName("btn_favorite_recipes")

        self.btn_my_recipes = QtWidgets.QPushButton(self.centralwidget)
        self.btn_my_recipes.setGeometry(QtCore.QRect(50, 250, 180, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_my_recipes.setFont(font)
        self.btn_my_recipes.setStyleSheet("background-color: rgb(138, 138, 138);\n"
"color: rgb(255, 255, 255);")
        self.btn_my_recipes.setObjectName("btn_my_recipes")

        self.btn_find_recipe = QtWidgets.QPushButton(self.centralwidget)
        self.btn_find_recipe.setGeometry(QtCore.QRect(70, 330, 150, 30))
        self.btn_find_recipe.setStyleSheet("background-color: rgb(178, 171, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_find_recipe.setObjectName("btn_find_recipe")
        self.btn_find_recipe.clicked.connect(lambda: self.controller.showMainScreen())#showMainScreen

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Profile)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(Profile)
        QtCore.QMetaObject.connectSlotsByName(Profile)

    def retranslateUi(self, Profile):
        _translate = QtCore.QCoreApplication.translate
        Profile.setWindowTitle(_translate("Profile", "???????????????????? ??????????"))
        self.text_name.setText(_translate("Profile", "??????????????????????????????"))
        self.btn_create_recipe.setText(_translate("Profile", "??????????????"))
        self.btn_exit.setText(_translate("Profile", "<-??????????"))
        self.btn_settings.setText(_translate("Profile", "??????????????????*"))
        self.btn_favorite_recipes.setText(_translate("Profile", "??????????????"))
        self.btn_my_recipes.setText(_translate("Profile", "????????"))
        self.btn_find_recipe.setText(_translate("Profile", "?????????? ????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Profile = QtWidgets.QMainWindow()
    ui = Ui_Profile()
    ui.setupUi(Profile)
    Profile.show()
    sys.exit(app.exec_())
