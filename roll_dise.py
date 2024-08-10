import random
class dise:
 def roll(self):
  numbers = (1,2,3,4,5,6)
  first= random.choice(numbers)
  secand= random.choice(numbers)
  return first,secand
s=dise()
print(s.roll())