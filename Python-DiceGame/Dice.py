# Dice Object
import random

class Dice:
  history = []

  def __init__(self, sideCount):
    self.sideCount = sideCount
    
  def getSideCount(self):
    return self.sideCount
  
  def rollDice(self):
    roll = random.randint(1,self.sideCount)
    #print("Rolled: " + str(roll))
    self.history.append(roll)
    return roll
  
  def getHistory(self):
    return self.history
