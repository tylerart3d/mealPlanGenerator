from PySide.QtGui import *
from PySide.QtCore import *
import sys
import stylesheet
import yaml
from random import shuffle
import meal
from meal import Meal
from functools import partial
import logging

reload(meal)


class Window(QDialog):

    days = ['Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday']

    path = 'meals.yaml'

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowMinMaxButtonsHint)
        self.setStyleSheet(stylesheet.main())
        self.createUI()
        self.createMeals()
        self.resize(1200, 600)


    def createUI(self):

        self.mealUI = {}
        self.meals = []

        mainLayout = QVBoxLayout()
        daysLayout = QHBoxLayout()

        self.create = QPushButton('Create Meal Plan')
        self.create.clicked.connect(self.createMenu)

        for day in self.days:
            label = QLabel(day)
            self.mealUI[day] = QTextEdit()
            refresh = QPushButton('Refresh')
            healthier = QPushButton('Healthier')
            healthier.clicked.connect(partial(self.healthier, day))

            easier = QPushButton('Easier')
            easier.clicked.connect(partial(self.easier, day))

            layout = QVBoxLayout()
            layout.addWidget(label)
            layout.addWidget(self.mealUI[day])
            layout.addWidget(refresh)
            layout.addWidget(healthier)
            layout.addWidget(easier)

            daysLayout.addLayout(layout)

        mainLayout.addWidget(self.create)
        mainLayout.addLayout(daysLayout)

        self.setLayout(mainLayout)


    def createMeals(self):

        with open(self.path, 'r') as f:
            data = yaml.load(f)

        for item in data:
            meal = Meal(item['name'])
            meal.setProtein(item['protein'])
            meal.setHealth(item['health'])
            meal.setFrequency(item['frequency'])
            meal.setDifficulty(item['difficulty'])
            self.meals.append(meal)


    def createMenu(self):

        # Generate list of meals
        masterList = []
        for meal in self.meals:
            # Assign Multiples by Frequency
            for i in range(meal.getFrequency()):
                masterList.append(meal)

        # Randomize List
        shuffle(masterList)

        # Get Fisrt 7 Meals
        weeklyMeals = []
        i = 0
        fish = False
        for meal in masterList:
            if i == 7:
                break

            if meal not in weeklyMeals:
                # Only 1 Fish a Week
                if meal.getProtein() == 'Fish':
                    if not fish:
                        fish = True
                        weeklyMeals.append(meal)
                        i += 1
                else:
                    weeklyMeals.append(meal)
                    i += 1

        # Add to UI
        i=0
        for day in self.days:
            self.mealUI[day].setText(weeklyMeals[i].getName())
            i+=1


    def refresh(self, day):
        pass



    def healthier(self, day):
        origMeals = {}
        for d in self.days:
            origMeals[d] = [m for m in self.meals if m.getName() == self.mealUI[d].toPlainText()][0]
        origMeal = origMeals[day]

        # Generate list of meals
        masterList = []
        for meal in self.meals:
            # Assign Multiples by Frequency
            for i in range(meal.getFrequency()):
                masterList.append(meal)

        # Randomize List
        shuffle(masterList)
        masterList = [m for m in masterList if m.getHealth() > origMeal.getHealth() and m not in origMeals]
        if not masterList:
            logging.error('No Healthier Meal Found')
            return

        self.mealUI[day].clear()
        self.mealUI[day].setText(masterList[0].getName())



    def easier(self, day):
        origMeals = {}
        for d in self.days:
            origMeals[d] = [m for m in self.meals if m.getName() == self.mealUI[d].toPlainText()][0]
        origMeal = origMeals[day]

        # Generate list of meals
        masterList = []
        for meal in self.meals:
            # Assign Multiples by Frequency
            for i in range(meal.getFrequency()):
                masterList.append(meal)

        # Randomize List
        shuffle(masterList)
        masterList = [m for m in masterList if m.getDifficulty() < origMeal.getDifficulty() and m not in origMeals]
        if not masterList:
            logging.error('No Easier Meal Found')
            return

        self.mealUI[day].clear()
        self.mealUI[day].setText(masterList[0].getName())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())
