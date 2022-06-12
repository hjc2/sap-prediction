from unicodedata import name


class Animal:
    kind = "pet"
    def __init__(self,name, attack, health):
        self.attack = attack
        self.health = health
        self.name = name
    def __repr__(self):
        return "(" + str(self.name) + ", " + str(self.attack) + ", " + str(self.health) + ")"
    def __str__(self):
        return "(" + str(self.name) + ", " + str(self.attack) + ", " + str(self.health) + ")"