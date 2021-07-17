# Derived class

#from oop_language.multilevel_inheritance.motherClass import Mother

import motherClass

class Doughter(motherClass.Mother):
    def __init__(self,dotname, mothername, grandmothername):
        self.dotname = dotname
 
        # invoking constructor of Mother class
        motherClass.Mother.__init__(self, mothername, grandmothername)
 
    def print_name(self):
        print('Grandmother name :', self.grandmothername)
        print("Mothername name :", self.mothername)
        print("Doughter name :", self.dotname)
 
#  Driver code
s1 = Doughter('IEEE', 'Maaaaa', 'me :)')
print(s1.grandmothername)
s1.print_name()