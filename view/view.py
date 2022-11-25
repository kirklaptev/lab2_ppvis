from view.screen.ChangeRecipe import Ui_ChangeRecipe
from view.screen.Entry_account import Ui_Entry_account
from view.screen.Profile import Ui_Profile
from view.screen.MainScreen import Ui_MainScreen
from view.screen.First import Ui_First
from view.screen.Settings import Ui_Settings
from view.screen.Sort import Ui_Sort
from view.screen.Recipe import Ui_Recipe

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class View:
    def __init__(self, c, m):
        self.model = m
        self.controller = c

        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()

        self.ChangeRecipe = Ui_ChangeRecipe(self.controller,self.model)
        self.Entry_account = Ui_Entry_account(self.controller,self.model)
        self.Profile = Ui_Profile(self.controller,self.model)
        self.MainScreen = Ui_MainScreen(self.controller,self.model)
        self.First = Ui_First(self.controller,self.model)
        self.Settings = Ui_Settings(self.controller,self.model)
        self.Sort = Ui_Sort(self.controller,self.model)
        self.Recipe = Ui_Recipe(self.controller,self.model)


    def show_First(self):
        self.Entry_account.hide()
        self.Profile.hide()
        self.First.show()
        sys.exit(self.app.exec_())

    def show_Create(self):
        self.Profile.hide()
        self.Entry_account.show()

    def show_Profile(self):
        self.First.hide()
        self.Settings.hide()
        self.MainScreen.hide()
        self.Profile.show()

    def show_Settings(self):
        self.Profile.hide()
        self.First.hide()
        self.Settings.show()

    def show_MainScreen(self):
        self.Profile.hide()
        self.Recipe.hide()
        self.MainScreen.show()

    def show_Recipe(self):
        self.MainScreen.hide()
        self.ChangeRecipe.hide()
        self.Recipe.show()

    def show_ChangeRecipe(self):
        self.Recipe.hide()
        self.ChangeRecipe.show()


    def show_Sort(self):
        self.MainScreen.hide()
        self.Sort.show()
