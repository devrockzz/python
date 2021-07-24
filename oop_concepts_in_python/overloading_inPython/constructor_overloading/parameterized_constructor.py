class Addition:
    first = 0
    second = 0
    answer = 0
    xyz = "bazinga!!!"
      
    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s
        self.xyz
      
    def display(self):
        print("instantiating the object with the help of const = "+ self.xyz)
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))#passing the parameter answer
  
    def calculate(self):
        self.answer = self.first + self.second
  
# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000) 
  
# perform Addition
obj.calculate() #calling the method
  
# display result
obj.display() # calling the method