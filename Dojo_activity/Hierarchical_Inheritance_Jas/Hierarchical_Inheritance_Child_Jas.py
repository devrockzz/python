import Hierarchical_Inheritance_Parent_Jas

#Derived Class1  

class Indian(Hierarchical_Inheritance_Parent_Jas.Food):
      def indianfood(self):
          print("Here is your Indian food!\n")
          self.p = "Paratha"
          self.q =  "Samosa"
          print(self.p,"is made of",self.a,",",self.y,",",self.e,"and",self.f,".")
          print(self.q,"is made of",self.a,",",self.c,",",self.x,",",self.y,",",self.e,"and",self.f,".\n")

#Derived Class2

class Italian(Hierarchical_Inheritance_Parent_Jas.Food):
      def italianfood(self):
          print("Here is your Italian food!\n")
          self.r = "Pasta"
          self.s = "Pizza"
          print(self.r,"is made of",self.a,",",self.e,",",self.b,",",self.x,",",self.y,",",self.z,"and",self.f,".")
          print(self.s,"is made of",self.a,",",self.e,",",self.d,"or",self.c,",",self.y,",",self.z,"and",self.f,".\n")

#Derived Class3

class Chinese(Hierarchical_Inheritance_Parent_Jas.Food):
      def chinesefood(self):
          print("Here is your Chinese food!\n")
          self.u = "Chow Mein"
          self.v = "Dumplings"
          self.w = "Noodles"
          print(self.u,"is made of",self.w,",",self.e,",",self.y,",",self.c,",",self.z,"and",self.f,".")
          print(self.v,"is made of",self.a,",",self.e,",",self.d,"or",self.c,",",self.x,"and",self.y,".\n")

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