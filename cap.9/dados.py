from random import randint
class Dice:
    def __init__ (self, sides = 6):
        self.sides = sides

    def roll_dice (self):
        print(randint(1, self.sides))
    
dado = Dice(10)
dado.roll_dice()