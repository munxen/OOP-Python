#Write a program that has a main class Games with a static field Year, describe
# the constructor assigning a value to the Year field, also describe the getName method, 
# which returns the name of the game. Based on the main class by inheritance, describe 
# four classes of PCGames, PS4Games, XboxGames, MobileGames. Add to each class 
# additional fields and redefine the getName method for all classes.

class Games:

    """Static field Year"""
    year = 'default year'

    """Constructor that assigns a value to the Year field"""
    def __init__(self,gy):
        self.year = gy

    """The getName method that returns the name of the game"""
    def getName(self,name):
        print ("Game name is " + name)
        return name


class PCGames(Games):
    platform = 'Computer games'
    def __init__(self, name):
        self.getName(name)

class PS4Games(Games):
    platform = 'Games for Play Station 4'
    def __init__(self, name):
        self.getName(name)

class XboxGames(Games):
    platform = 'Games for XBOX'
    def __init__(self, name):
        self.getName(name)

class MobileGames(Games):
    platform = 'Mobile games'
    def __init__(self, name):
        self.getName(name)

"""tests"""
game_1 = PCGames("Call of Duty")
print (game_1.platform)
print ("Game year is " + game_1.year)
game_1.year = '2010'
print ("Game year is " + game_1.year)
print ("---------")
game_2 = PS4Games("Marvel")
print (game_2.platform)
game_2.year = '2014'
print ('Game year is ' + game_2.year )