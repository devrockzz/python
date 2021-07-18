import parenTclass #whatever the property of the parent calss i will be able to cap[ture it and use it

class Child(parenTclass.Parent):
     def func2(self):
          print("This function is in child class.")




object = Child()
object.func1()
object.func2()