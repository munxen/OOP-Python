#Create a Soda class (to determine the type of carbonated water) that takes 1 argument
# during initialization (responsible for the additive to the selected lemonade).
#In this class, implement the show_my_drink() method, which prints Soda and {ADDITIVE}
# if there is an additive, otherwise the following phrase will be displayed: Regular soda.

class Soda():
    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Soda and {self.ingredient}')
        else:
            print('Regular soda')


"""tests"""

drink2 = Soda('struwberry')
drink3 = Soda(5)

drink2.show_my_drink()
drink3.show_my_drink()