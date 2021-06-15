#please look into the object class diagram to understand
class dogClass:
  def __init__(self, breed, size, age, color):
    self.breed = breed
    self.size = size
    self.age = age
    self.color = color

  def Eat(self):
    print("I love to eat Milk " + self.breed)
  def Sleep(self):
    print("I am very lazy human " + self.breed)
  def Sit(self):
    print("I just sit and watch cats " + self.breed)
  def Run(self):
    print("When i turn fat i love to run " + self.breed)

dataOne = dogClass("Nepolitan Mastiff", "Large", 5, "black")
dataTwo = dogClass("Maltis", "Small", 2, "White")
dataThree = dogClass("Chow Chow", "Medium", 3, "Brown")

dataOne.Eat()
dataTwo.Sleep()
dataThree.Sit()
dataOne.Run()