import issa_hierarchical
#child class 1
class dior(issa_hierarchical.brands):
 def func2(self):
        print("the latest dior haut couture is awesome")
#child class 2
class versace(issa_hierarchical.brands): 
   def func3(self):
        print("the new summer collection is lit.")
#child class 3
class chanel(issa_hierarchical.brands):   
    def func4(self):
        print("the new floral perfume is nostalgic")
o1 = dior()
o2 = versace()
o3 = chanel()
o1.func1()
o1.func2()
o2.func1()
o2.func3()
o3.func1()
o3.func4()