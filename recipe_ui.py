from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import sys
import stylesheet
import yaml
from random import shuffle
import meal
from meal import Meal
from functools import partial
import logging
from imp import reload

reload(meal)


class Window(QMainWindow):

    path = 'meals.yml'

    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.setStyleSheet(stylesheet.main())
        self.create_ui()
        self.load_recipes()
        self.resize(1200, 600)

    def update_recipe(self):
        self.list_ingredients.clear()
        self.list_directions.clear()

        menu_item = self.list_recipe.selectedItems()[0]
        self.label_name.setText(menu_item.text())

        ingredients = menu_item.meal_data['ingredients']
        for ingredient in ingredients:
            item = QTreeWidgetItem()
            item.setText(0, ingredient)
            try: item.setText(1, str(ingredients[ingredient]['amount']))
            except: pass
            try: item.setText(2, str(ingredients[ingredient]['cut']))
            except: pass
            try: item.setText(3, str(ingredients[ingredient]['notes']))
            except: pass

            self.list_ingredients.addTopLevelItem(item)
            self.list_ingredients.resizeColumnToContents(0)


        directions = menu_item.meal_data['directions']
        inst_string = ''
        for instruction in directions:
            inst_string += instruction + '\n\n'

        self.list_directions.setText(inst_string)


    def create_ui(self):

        # Widgets
        self.list_recipe = QListWidget()
        self.label_name = QLabel()
        self.list_ingredients = IngredientWidget()
        self.list_directions = QTextEdit()

        # Connections
        self.list_recipe.itemSelectionChanged.connect(self.update_recipe)

        # Layouts
        layout_ingredients = QVBoxLayout()
        layout_ingredients.addWidget(self.label_name)
        layout_ingredients.addWidget(self.list_ingredients)
        layout_ingredients.addWidget(self.list_directions)

        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(self.list_recipe)
        layout_horizontal.addLayout(layout_ingredients)

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_horizontal)
        layout_main.addWidget(QPushButton('test'))

        # Main Widget
        widget_main = QWidget()
        widget_main.setLayout(layout_main)
        self.setCentralWidget(widget_main)

    def load_recipes(self):
        with open(self.path, 'r') as f:
            data = yaml.safe_load(f)

        for meal in data['meals']:
            item = QListWidgetItem()
            item.setText(meal.title())
            item.meal_data = data['meals'][meal]
            self.list_recipe.addItem(item)


class IngredientWidget(QTreeWidget):

    def __init__(self):
        super(IngredientWidget, self).__init__()
        self.setHeaderLabels(['Ingredients', 'Amount', 'Cut', 'Info'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())