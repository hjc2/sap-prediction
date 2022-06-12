
from animal import Animal
from team import Team

x = Animal("frog", 5,5)
y = Animal("lemur",4,4)

print(x)
print(x.name)
print(x.kind)
x.kind = "alpha"
print(x.kind)
print(y.kind)

player = []
opp = []

player.append(Animal("Dog",5, 4))
player.append(Animal("Frog",3, 4))

opp.append(Animal("Dog",9, 4))
opp.append(Animal("Frog",9, 4))

def attack(p, o):
    o[0].health -= p[0].attack
    p[0].health -= o[0].attack

def removeDead(team):
    team = [i for i in team if i.health > 0]


print(player)
print(opp)
attack(player, opp)
print(player)
print("---")
print(player)
removeDead(player)
print(player)
print(".......")

dog = Animal("dog", -1,-1)
dog = Animal("frog", 2,1)

g = Team()
g.roster.append(dog)
print(g)
g.purgeDead()
print(g)
print(len(g))