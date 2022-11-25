from view.view import View
from model.model import CookBook, Ingredient, Recipe, Profile, Creater_of_recipes, Sorter, Section, SortType



class Controller:
    def __init__(self, model):
        self.model = model
        self.view = View(self, self.model)

    def showFirst(self):
        self.view.show_First()

    def showCreate(self):
        self.view.show_Create()

    def showProfile(self):
        self.view.show_Profile()

    def showSettings(self):
        self.view.show_Settings()

    def showMainScreen(self):
        self.view.show_MainScreen()

    def showRecipe(self):
        self.view.show_Recipe()

    def showChangeRecipe(self):
        self.view.show_ChangeRecipe()

    def showSort(self):
        self.view.show_Sort()