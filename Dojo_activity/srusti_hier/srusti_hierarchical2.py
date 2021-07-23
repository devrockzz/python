import srusti_hierarchical1
#child class 1
class apple(srusti_hierarchical1.fruits):
 def func2(self):
        print("apples are filled with nutrients.")
#child class 2
class mango(srusti_hierarchical1.fruits): 
   def func3(self):
        print("mango is my favourite fruit.")
#child class 3
class guava(srusti_hierarchical1.fruits):   
    def func4(self):
        print("guava are the best seasonal fruit.")
o1 = apple()
o2 = mango()
o3 = guava()
o1.func1()
o1.func2()
o2.func1()
o2.func3()
o3.func1()
o3.func4()