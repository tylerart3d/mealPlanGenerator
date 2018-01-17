from PySide.QtGui import *
from PySide.QtCore import *
import sys
import yaml
import random
import stylesheet

class Window(QDialog):

    days = ['Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday']

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowMinMaxButtonsHint)
        self.createUI()
        self.setStyleSheet(stylesheet.main())


    def createUI(self):

        self.meals = {}

        mainLayout = QVBoxLayout()
        daysLayout = QHBoxLayout()

        create = QPushButton('Create Meal Plan')
        create.clicked.connect(self.createMealPlan)

        for day in self.days:
            label = QLabel(day)
            self.meals[day] = QTextEdit()
            refresh = QPushButton('Refresh')
            healthier = QPushButton('Healthier')
            easier = QPushButton('Easier')

            layout = QVBoxLayout()
            layout.addWidget(label)
            layout.addWidget(self.meals[day])
            layout.addWidget(refresh)
            layout.addWidget(healthier)
            layout.addWidget(easier)

            daysLayout.addLayout(layout)

        mainLayout.addWidget(create)
        mainLayout.addLayout(daysLayout)

        self.setLayout(mainLayout)



    def createMealPlan(self):
        path = 'meals.yaml'
        with open(path, 'r') as f:
            data = yaml.load(f)

        masterList = []
        for i in data:
            masterList += [data.index(i)]*i['Frequency']

        random.shuffle(masterList)
        meals = []

        for i in masterList:
            if i not in meals:
                meals.append(i)

        for day in self.days:
            self.meals[day].clear()
            i = self.days.index(day)
            print i
            meal = data[meals[i]]['Name of Dish']
            self.meals[day].setText(meal)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec_())
