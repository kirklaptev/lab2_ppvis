from enum import Enum


class CookBook:
    def __init__(self):
        self.Profiles = []
        self.Recipes = []
        self.Sections = []
        self.List_of_ingridients = []

class Ingredient:
    def __init__(self, name_of_ingredient):
        self.name_of_ingredient = name_of_ingredient

class Recipe:
    def __init__(self, name_of_recipe, short_description, full_description, date, rating, time):
        self.name_of_recipe = name_of_recipe
        self.short_description = short_description
        self.full_description = full_description
        self.date = date
        self.rating = rating
        self.time = time
        self.Ingredients = []
        self.Sections_in_recipe = []

    def create_recipe(self, parametrs):
        pass

    def get_recipe(self):
        pass

    def get_annotations(self):
        pass

    def has_ingredient(self, ingredeint):
        pass

    def is_on_section(self, section):
        pass

class Profile:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.FavoriteRecipes = []
        self.MyRecipes = []

    def is_log_in(self):
        pass

    def log_in(self, name, password):
        pass

    def create_profile(self, name, password):
        pass

    def change_name(self, name):
        pass

    def change_password(self, password):
        pass

    def log_out(self):
        pass

    def delete_profile(self):
        pass

    def add_my_recipe(self, recipe):
        pass

    def add_favorite_recipe(self, recipe):
        pass

    def is_my_recipe(self, recipe):
        pass

    def is_favorite_recipe(self, recipe):
        pass


class Creater_of_recipes:
    def create_recipe(self):
        pass

    def get_recipe(self, recipe):
        pass

    def set_recipe(self, parametrs):
        pass

class Sorter:
    def __init__(self, name_of_sorter, type_of_sort):
        self.name_of_sorter = name_of_sorter
        self.type_of_sort = SortType(type_of_sort)
        self.Sort_sections = []
        self.Want_ingredients = []
        self.No_ingredients = []
    def get_parametrs(self):
        pass

    def set_parametrs(self, parametrs):
        pass

    def reset_parametrs(self):
        pass

class SortType(Enum):
    rating = 1
    time = 2
    date = 3

class Section:
    def __init__(self, name_of_section):
        self.name_of_section = name_of_section
