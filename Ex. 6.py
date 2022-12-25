class MightiestWeapon:
    name = 'Default name'
    def __init__(self, name):
        self.name = name
weapon = MightiestWeapon('sword')
#tests
print (MightiestWeapon.name)
print (weapon.name)

class Animal:
    def make_sound(self):
        print ("makes an animal sound")
class Cat(Animal):
    def make_cat(self):
        print ("Get up! I dropped everything..")
class Dog(Animal):
    def make_dog(self):
        print ("Wof,wof!")
#tests
Tom = Cat()
Tom.make_sound()
