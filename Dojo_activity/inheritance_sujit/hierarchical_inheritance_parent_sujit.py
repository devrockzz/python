
# Base Class

class Calculater:

    def add(self):
        self.a = 10
        self.b = 20
        print("\nAddition is: " , self.a + self.b)

    def sub(self):
        self.a = 50
        self.b = 40
        print("\nSubstraction is: " , self.a - self.b)

    def mul(self):
        self.a = 2
        self.b = 3
        print("\nMultiplication is: " , self.a * self.b)

    def div(self):
        self.a = 10
        self.b = 5
        print("\nDivision is: " , self.a // self.b)