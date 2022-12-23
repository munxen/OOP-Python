#It is necessary to implement the code shown in the examples above.
#Create a Rectangle class and a ToyClass class. For ToyClass,
# you need to add three attributes, and the method that sets them.

class Rectangle ():
    """creating a rectangle """
    def __init__(self, width, height):
        """requesting width and height"""
        self.width = width
        self.height = height
    def getWidth(self):
        """output rectangle widtg"""
        return self.width
    def getHeight(self):
        """output rectangle height"""
        return self.height
    def getArea(self):
        """counting the rectangle area"""
        return self.height*self.width

"""tests class Rectabgle"""
rect1 = Rectangle(5,7)
rect2 = Rectangle(2,5)
rect3 = Rectangle(10,49)
print("Rectangle width is " + str(rect1.getWidth()))
print("Rectangle height is " + str(rect2.getHeight()))
print("Rectangle area is " + str(rect3.getArea()))


class ToyClass():
    "toy description class"
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country
        """formats data neatly"""
    def getFullName(self):
        print ("You toy is " + self.name)
        print ("He is " + str(self.age) + " years old.")
        print ("He was born in " + self.country)

"""tests class ToyClass"""
toy1 = ToyClass('Boby',13,'France')
toy1.getFullName()
