import fatherClass, motherClass

class Child(fatherClass.Father, motherClass.Mother):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

  
# Driver's code
s1 = Child()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
