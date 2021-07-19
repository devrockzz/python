import Hierar_Suk
#child class 1
class HMV(Hierar_Suk.automobiles):
    def func2(self):
        print("I want the parts of High Motor Vehicles.")
#child class 2
class MMV(Hierar_Suk.automobiles):
    def func3(self):
        print("I want the parts of Medium Motor Vehicles.")
#child class 3
class LMV(Hierar_Suk.automobiles):
    def func4(self):
        print("I want the parts of Lower Motor Vehicles.")
o1 = HMV()
o2 = MMV()
o3 = LMV()
o1.func1()
o1.func2()
o2.func1()
o2.func3()
o3.func1()
o3.func4()