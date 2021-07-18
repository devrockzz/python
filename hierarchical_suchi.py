# Python program to demonstrate
# Hierarchical inheritance
class kitchen:
    def ingredients(self):
        self.A="Spices"
        self.B="rice"
        self.C="dal"
        self.D="sauces"
        self.E="chicken"
        
        
 
# Derived class1
class Indian(kitchen):
      def indianfood(self):
          self.x = "water"
          self.y =  self.B
          self.z =  self.C
          print("Here is my dishes", "\n")
          print("INDIANFOOD!!","\n")
          print("This indian food rice, dal, chicken made of:" ,self.y, "," ,self.z ,",", self.E, "," ,self.A, '&', self.x, "\n" )
          
# Derivied class2
class chinese(kitchen):
      def chinesefood(self):
          self.o = "noodles"
          print("CHINESEFOOD!!", "\n")
      

          print("This chinese food chowmin made of: ", self.o, ",",self.A ,"&" , self.D, "\n")
  # Driver's code
class italian(kitchen):
      def italianfood(self):
        self.g = "flour"
        self.h = "chese"
        print("ITALIANFOOD!!", "\n")
        print("This italian food pizza made of:", self.g, "," , self.h, "&",self.D)
object1 = Indian()
object1.ingredients()
object1.indianfood()
object2 = chinese()
object2.ingredients()
object2.chinesefood()
object3 = italian()
object3.ingredients()
object3.italianfood()