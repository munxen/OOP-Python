#Write a program with a Student class that has three
# attributes: name, GroupNumber, and age. By default,
# name = Ivan, age = 18, GroupNumber = 10A. You need
# to create five methods: getName, getAge, getGroupNumber,
# setNameAge, setGroupNumber. The getName method is
# needed to get data about the name of a particular
# student, the getAge method is needed to get data about
# the age of a particular student, the Setgroupnumber
# method is needed to get data about the group number
# of a particular student. The SetNameAge method allows
# you to change the data of the attributes set by default,
# the setGroupNumber method allows you to change the group
# number set by default. In the program, you need to
# create five instances of the Student class, set them
# different names, age and group number.

class Student():
    "initializes the data of a specific student"
    def __init__(self,name = 'Ivan',groupNumber = '10A',age = 18):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def getName(self):
        "output student name"
        print ("Name student is " + self.name + ".")

    def getAge(self):
        "output student age"
        print("Student age is " + str(self.age))

    def getGroupNumber(self):
        "output student group"
        print ("Student group is " + self.groupNumber)

    def setNameAge(self,NewName):
        "changes standard name"
        self.name = NewName

    def setGroupNumber(self,NewGroup):
        "changes standard group number"
        self.groupNumber = NewGroup

"""tests"""
#student1
studen1 = Student()
studen1.getName()
studen1.getAge()
studen1.getGroupNumber()
print("--------")
#student2
student2 = Student()
student2.setNameAge('Lucy')
student2.setGroupNumber('11B')
student2.getName()
student2.getAge()
student2.getGroupNumber()
