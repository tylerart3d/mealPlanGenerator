

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
        return self.get_name() == other.get_name()

    def get_name(self):
        return self._name

    def get_protein(self):
        return self._protein

    def get_health(self):
        return self._health

    def get_frequency(self):
        return self._frequency

    def get_difficulty(self):
        return self._difficulty

    def set_name(self, name):
        self._name = name

    def set_protein(self, protein):
        self._protein = protein

    def set_health(self, health):
        self._health = health

    def set_frequency(self, frequency):
        self._frequency = frequency

    def set_difficulty(self, difficulty):
        self._difficulty = difficulty