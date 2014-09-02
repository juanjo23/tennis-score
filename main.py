class Game:
  """
  Shows the score of a tennis game
  Example:
  >>> game = Game('Nadal', 'Delbonis')
  >>> game.scores(1).scores(2).scores(1).scoreboard()
  [30, 15]
  >>> game.scores(1).scores(1).scoreboard()
  [Nadal wins]
  
  A longer match:
  >>> game2 = Game('Nadal', 'Federer')
  >>> game2.scores(1).scores(2).scores(1).scores(1).scores(2).scoreboard()
  [40, 30]
  >>> game2.scores(2).scoreboard()
  [deuce]
  >>> game2.scores(1).scores(2).scores(2).scoreboard()
  [--, advantaje]
  >>> game2.scores(1).scoreboard()
  [deuce]
  >>> game2.scores(2).scores(2).scoreboard()
  [Federer wins]
  """
  def __init__(self, name1, name2):
    self.name1 = name1
    self.name2 = name2
    self.a = 0
    self.b = 0

  def scores(self, player):
    if(player == 1):
      self.a = 15 if self.a==0 else (30 if self.a==15 else (40 if self.a==30 else self.a+1))
    else:
      self.b = 15 if self.b==0 else (30 if self.b==15 else (40 if self.b==30 else self.b+1))
    return self

  def scoreboard(self):
    if self.a >= 40 and self.b >= 40 and self.a == self.b:
      print("[deuce]")
    elif self.a > 40 and self.a - self.b == 1:
      print("[advantaje, --]")
    elif self.b > 40 and self.b - self.a == 1:
      print("[--, advantaje]") 
    elif self.a > 40 and self.a - self.b > 1:
      print("[%s wins]" % self.name1)
    elif self.b > 40 and self.b - self.a > 1:
      print("[%s wins]" % self.name2)
    else:
      print("[%d, %d]" % (self.a, self.b))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
