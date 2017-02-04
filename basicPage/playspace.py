# from playground.py import afunction
# from playground.py import *

class Person:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def printName(self):
        print(self.name)

    def printHeight(self):
        print(self.height)

    def printWeight(self):
        print(self.weight)


dude = Person('this person', 'average', 'regular')

dude.printName()
dude.printHeight()
dude.printWeight()

# -------- This should be a new file! ---------------------------------------

class Other(Person):
    def __init__(self, otherness, name, height, weight):
        Person.__init__(self, name, height, weight)
        self.otherness = otherness

    def printOtherness(self):
        print(self.otherness)

dudette = Other('strange', 'dudette', 'squat', 'comfy')

dudette.printOtherness()
