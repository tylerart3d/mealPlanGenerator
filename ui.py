from PySide.QtGui import *
from PySide.QtCore import *
import sys
import json

class Window(QDialog):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowMinMaxButtonsHint)
        self.createUI()


    def createUI(self):

        days = ['Sunday',
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday']

        self.meals = {}

        mainLayout = QVBoxLayout()
        daysLayout = QHBoxLayout()

        create = QPushButton('Create Meal Plan')
        create.clicked.connect(self.createMealPlan)

        for day in days:
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
        path = 'meals.json'
        with open(path, 'r') as f:
            data = json.load(f)

            import pprint
            pprint.pprint(data)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec_())
