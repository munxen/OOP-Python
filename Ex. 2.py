#Nikolai needs to check whether it is possible to form a triangle from the presented
# segments of conditional length. To do this, he decided to create a TriangleChecker
# class that accepts only positive numbers.Using the is_triangle() method, the following 
# values are returned (depending on the situation):
#Hooray, you can build a triangle!;
#Nothing will work with negative numbers!;
#You only need to enter numbers!;
#It's a pity, but you can't make a triangle out of this.

class TriangleChecker():
    def __init__(self,num1,num2,num3): #we accept 3 numbers in different variables
        """Checking for entering numbers"""
        if isinstance(num1,int) and isinstance(num2,int) and isinstance(num3,int):
            self.num1 = num1
            self.num2 = num2
            self.num3 = num3
            self.b = True #lever for error output
            "Checking positive numbers"
            if num1>0 and num2>0 and num3>0:
                self.num1 = num1
                self.num2 = num2
                self.num3 = num3
                self.a = True #lever for error output
                """Checking the triangle rule"""
                if num1+num2>num3 and num1+num3>num2 and num2+num3>num1:
                    self.num1 = num1
                    self.num2 = num2
                    self.num3 = num3
                    self.c = True #lever for error output
                else:
                    self.c = False 
                    return
            else:
                self.a = False
                return
        else:
            self.b = False
            return


        
    def is_triangle(self):
        if self.b == False: #we use levers to output errors
            print ("You only need to enter numbers!")
            return
        elif self.a == False:
            print ("Nothing will work with negative numbers")
            return
        elif self.c == False:
            print ("It's a pity, but you can't make a triangle out of this.")
            return
        else: #if all checks are passed
            print ("Hooray, you can build a triangle!")

"""tests"""
triangle1 = TriangleChecker(2, 3, 4)
triangle1.is_triangle()
triangle2 = TriangleChecker(77, 3, 4)
triangle2.is_triangle()
triangle3 = TriangleChecker(77, 3, 'slide 3')
triangle3.is_triangle()
triangle4 = TriangleChecker(77, -3, 4)
triangle4.is_triangle()