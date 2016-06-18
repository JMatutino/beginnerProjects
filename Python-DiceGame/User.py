# User Object
class User:
  
  def __init__(self, playerNum, diceSideCount):
    self.playerNum = playerNum
    self.stats = [0] * diceSideCount
  
  def addStats(self, numRolled):
    self.stats[numRolled - 1] = self.stats[numRolled - 1] + 1
    
  def getStats(self):
    for sideNum, count in enumerate(self.stats):
      print("{}: {}".format(sideNum + 1, count))
    return self.stats
    

  