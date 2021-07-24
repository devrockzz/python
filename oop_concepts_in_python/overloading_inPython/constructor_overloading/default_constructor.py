class StudydefaultConstr:
  
    # default constructor
    def __init__(self):
        self.geek = "We are good"
  
    # a method for printing data members
    def print_Geek(self):
        print(self.geek)
  
  
# creating object of the class
obj = StudydefaultConstr()
  
# calling the instance method using the object obj
obj.print_Geek()