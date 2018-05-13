

class Meal(object):

    def __init__(self, name):
        self._name = name
        self._protein = None
        self._health = None
        self._frequency = None
        self._difficulty = None


    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name

    def __eq__(self, other):
        return self.getName() == other.getName()

    def getName(self):
        return self._name

    def getProtein(self):
        return self._protein

    def getHealth(self):
        return self._health

    def getFrequency(self):
        return self._frequency

    def getDifficulty(self):
        return self._difficulty

    def setName(self, name):
        self._name = name

    def setProtein(self, protein):
        self._protein = protein

    def setHealth(self, health):
        self._health = health

    def setFrequency(self, frequency):
        self._frequency = frequency

    def setDifficulty(self, difficulty):
        self._difficulty = difficulty