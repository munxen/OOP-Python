#Написать программу, в которой есть главный класс Games со статическим полем Year, 
# опишите конструктор присваивающий значение полю Year, также опишите метод getName, 
# который возвращает имя игры. На основе главного класса путем наследования опишите 
# четыре класса PCGames, PS4Games, XboxGames, MobileGames. Добавьте каждому классу 
# дополнительные поля и переопределите у всех классов метод getName.

class Games:

    """Статическое поле Year"""
    year = 'default year'

    """Конструктор присваивающий значение полю Year"""
    def __init__(self,gy):
        self.year = gy

    """Метод getName который возвращает имя игры"""
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