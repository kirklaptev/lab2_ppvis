# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel, QWidget)


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainScreen(QMainWindow, object):
    def __init__(self, c, m):
        super().__init__()
        self.model = m
        self.controller = c
        MainScreen = QWidget()

        self.setObjectName("MainScreen")
        self.resize(300, 400)
        self.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.centralwidget = QtWidgets.QWidget(MainScreen)
        self.centralwidget.setObjectName("centralwidget")

        self.btn_profile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_profile.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.btn_profile.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(156, 156, 156);")
        self.btn_profile.setObjectName("btn_profile")
        self.btn_profile.clicked.connect(lambda: self.controller.showProfile())#showProfile

        self.btn_find = QtWidgets.QPushButton(self.centralwidget)
        self.btn_find.setGeometry(QtCore.QRect(150, 0, 150, 30))
        self.btn_find.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(156, 156, 156);")
        self.btn_find.setObjectName("btn_find")

        self.btn_name_of_recipe = QtWidgets.QPushButton(self.centralwidget)
        self.btn_name_of_recipe.setGeometry(QtCore.QRect(0, 50, 300, 30))
        self.btn_name_of_recipe.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"color: rgb(170, 0, 255);")
        self.btn_name_of_recipe.setObjectName("btn_name_of_recipe")
        self.btn_name_of_recipe.clicked.connect(lambda: self.controller.showRecipe())#showRecipe


        self.text_short_description = QtWidgets.QLabel(self.centralwidget)
        self.text_short_description.setGeometry(QtCore.QRect(0, 80, 300, 80))
        self.text_short_description.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"")
        self.text_short_description.setObjectName("text_short_description")

        self.btn_like = QtWidgets.QPushButton(self.centralwidget)
        self.btn_like.setGeometry(QtCore.QRect(0, 160, 60, 30))
        self.btn_like.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"color: rgb(170, 0, 255);")
        self.btn_like.setObjectName("btn_like")

        self.text_likes = QtWidgets.QLabel(self.centralwidget)
        self.text_likes.setGeometry(QtCore.QRect(60, 160, 30, 30))
        self.text_likes.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"")
        self.text_likes.setObjectName("text_likes")

        self.text_type_of_recipe = QtWidgets.QLabel(self.centralwidget)
        self.text_type_of_recipe.setGeometry(QtCore.QRect(90, 160, 150, 30))
        self.text_type_of_recipe.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"")
        self.text_type_of_recipe.setObjectName("text_type_of_recipe")
        self.text_time = QtWidgets.QLabel(self.centralwidget)
        self.text_time.setGeometry(QtCore.QRect(240, 160, 60, 30))
        self.text_time.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"")
        self.text_time.setObjectName("text_time")
        self.text_date = QtWidgets.QLabel(self.centralwidget)
        self.text_date.setGeometry(QtCore.QRect(210, 52, 90, 25))
        self.text_date.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"")
        self.text_date.setObjectName("text_date")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainScreen)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "???????????????????? ??????????"))
        self.btn_profile.setText(_translate("MainScreen", "??????????????"))
        self.btn_find.setText(_translate("MainScreen", "??????????"))
        self.btn_name_of_recipe.setText(_translate("MainScreen", "????????????                                            25 ?????? 2022"))
        self.text_short_description.setText(_translate("MainScreen", "???????????????????????? ???????????????????? ???????????? ?? ?????????????????? \n"
"????????????????, ?????????????????? ???????????????? ?? ?????????????? \n"
"??????????????????"))
        self.btn_like.setText(_translate("MainScreen", "????????"))
        self.text_likes.setText(_translate("MainScreen", "254"))
        self.text_type_of_recipe.setText(_translate("MainScreen", "????????????, ??????????, ?????????????????????? ??????????"))
        self.text_time.setText(_translate("MainScreen", "  40 ??????."))
        self.text_date.setText(_translate("MainScreen", "25 ???????? 2022"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainScreen = QtWidgets.QMainWindow()
    ui = Ui_MainScreen()
    ui.setupUi(MainScreen)
    MainScreen.show()
    sys.exit(app.exec_())
