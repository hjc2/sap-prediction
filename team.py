
from urllib import robotparser
from animal import Animal


class Team:
    name = "alpha"
    def __init__(self):
        self.roster = []
    def __repr__(self):
        return str(self.roster)
    def __str__(self):
        return str(self.roster)
    def __len__(self):
        return len(self.roster)

    def purgeDead(self):
        self.roster = [x for x in self.roster if x.health > 0]