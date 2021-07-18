
# Base Class

class Calculater:

    def add(self):
        self.a = 10
        self.b = 20
        print("Addition is " , self.a + self.b)

    def sub(self):
        self.a = 30
        self.b = 40
        print("Substraction is " , self.a - self.b)

    def mul(self):
        self.a = 2
        self.b = 3
        print("Multiplication is : " , self.a * self.b)

    def div(self):
        self.a = 10
        self.b = 5
        print("Division is : " , self.a // self.b)

#  Child Class - 1       

class Square(Calculater):

    def square(self):
        self.a = 25
        print("Square of " , self.a , " is " , self.a * self.a)

#  Child Class - 2

class Factorial(Calculater):

    def fact(self):
        self.i = 1
        self.n = 5
        self.fact = 1
        for i in range(self.i , self.n + 1):
            self.fact = self.fact * i
        print("Factorial is : " , self.fact)

Sq = Square()

fac = Factorial()

Sq.add()

Sq.sub()

fac.mul()

fac.div()

Sq.square()

fac.fact()




    