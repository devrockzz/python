class food():
# init method or constructor
    def __init__(self,fruit, color):
        self.fruit = fruit
        self.color = color
       
 
    def show(self):
        print(self)
        print(self.__dict__)
        print("fruit is", self.fruit)
        print("color is", self.color )
        
 
apple = food("apple", "red")
grapes = food("grapes", "green")
 
apple.show()
grapes.show()
#food object->{"apple", "red","grapes", "green"} = 0x000000C3A1EA2C50
