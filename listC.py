
from animal import Animal

a = [Animal("dog", 1,1), Animal("frog", 1,2), Animal("toad", 2,2)]
print(a)
a = [x for x in a if x.health > 0]
print(a)
