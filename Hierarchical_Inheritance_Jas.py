print("Hello, welcome to my restaurant !!\n")

#Base Class

class Food:
      def food_ingredients(self):
          self.x = "Spices"
          self.y = "Salt"
          self.z = "Sauce"
          self.a = "Flour"
          self.b = "Eggs"
          self.c = "Vegetables" 
          self.d = "Meat"
          self.e = "Water"
          self.f = "Cooking oil"
          print("Food Menu:")

#Derived Class1  

class Indian(Food):
      def indianfood(self):
          print("Here is your Indian food!\n")
          self.p = "Paratha"
          self.q =  "Samosa"
          print(self.p,"is made of",self.a,",",self.y,",",self.e,"and",self.f,".")
          print(self.q,"is made of",self.a,",",self.c,",",self.x,",",self.y,",",self.e,"and",self.f,".\n")

#Derived Class2

class Italian(Food):
      def italianfood(self):
          print("Here is your Italian food!\n")
          self.r = "Pasta"
          self.s = "Pizza"
          print(self.r,"is made of",self.a,",",self.e,",",self.b,",",self.x,",",self.y,",",self.z,"and",self.f,".")
          print(self.s,"is made of",self.a,",",self.e,",",self.y,",",self.z,"and",self.f,".\n")

#Derived Class3

class Chinese(Food):
      def chinesefood(self):
          print("Here is your Chinese food!\n")
          self.u = "Chow Mein"
          self.v = "Dumplings"
          self.w = "Noodles"
          print(self.u,"is made of",self.w,",",self.e,",",self.y,",",self.c,",",self.z,"and",self.f,".")
          print(self.v,"is made of",self.a,",",self.e,",",self.x,",",self.y,"and",self.c,".\n")

#Driver's Code

object1 = Indian()
object2 = Italian()
object3 = Chinese()
object1.food_ingredients()
object1.indianfood()
object2.food_ingredients()
object2.italianfood()
object3.food_ingredients()
object3.chinesefood()