from model.model import CookBook, Ingredient, Recipe, Profile, Creater_of_recipes, Sorter, Section, SortType
from controller.controller import Controller

class Main:
    def __init__(self):
        self.model = CookBook, Ingredient, Recipe, Profile, Creater_of_recipes, Sorter, Section, SortType
        self.controller = Controller(self.model)

    def build(self):
        self.controller.showFirst()

if __name__ == '__main__':
    main = Main()
    main.build()