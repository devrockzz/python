

import hierarchical_inheritance_parent_sujit 

#  Child Class - 1       

class Square(hierarchical_inheritance_parent_sujit.Calculater):

    def square(self):
        self.a = 25
        print("\nSquare of " , self.a , " is: " , self.a * self.a)

#  Child Class - 2

class Factorial(hierarchical_inheritance_parent_sujit.Calculater):

    def fact(self):
        self.i = 1
        self.n = 5
        self.fact = 1
        for i in range(self.i , self.n + 1):
            self.fact = self.fact * i
        print("\nFactorial is: " , self.fact , "\n")

Sq = Square()

fac = Factorial()

Sq.add()

Sq.sub()

fac.mul()

fac.div()

Sq.square()

fac.fact()




    