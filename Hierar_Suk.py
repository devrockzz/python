class automobiles:
    def func1(self):
        print("I have all the spare parts.")
class HMV(automobiles):
    def func2(self):
        print("I want the parts of High Motor Vehicle.")
class MMV(automobiles):
    def func3(self):
        print("I want the parts of Medium Motor Vehicles.")
class LMV(automobiles):
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