from Dice import Dice
from User import User

dice = Dice(6)
user1 = User(1, dice.getSideCount())

i = 0
while i < 100:
  print("Roll#: " + str(i))
  roll = dice.rollDice()
  print("~ " + str(roll))
  user1.addStats(roll)
  print("---------")
  i = i + 1
  
print("\nUser stats: ")
user1.getStats()
