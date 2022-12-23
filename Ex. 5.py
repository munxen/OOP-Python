#Write a program with the Car class. Create a constructor for the Car class. 
#Create attributes of the Car class — color (color), type (type), year (year). 
#Write five methods. The first is the start of the car, when it is called, the 
# message "The car is started" is displayed. The second one — turning off the 
# car — displays the message "The car is turned off". The third is the assignment 
# of the year of manufacture to the car. The fourth method is assigning a type to a car. 
#The fifth is assigning a color to the car.

class Car():

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def startCar(self):
        print ("The car is started.")

    def stopCar(self):
        print ("The car is silenced.")

    def carYear(self,year):
        "Change car year"
        self.year = year
    
    def carType(self,type):
        "Change car year"
        self.type = type
    
    def carColor(self,color):
        "Change car year"
        self.color = color

    def carInfo(self):
        """Machine data"""
        print ("\nCar pecifications: ")
        print ("Color: " + self.color)
        print ("Type: " + self.type)
        print ("Year " + self.year)

"""tests"""
car1 = Car('blue' , 'sportcar', '2002')
car1.startCar()
car1.carInfo()
car1.carYear('2020')
car1.carColor('black')
car1.carInfo()
car1.stopCar()