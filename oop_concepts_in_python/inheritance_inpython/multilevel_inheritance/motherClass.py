import grandMotherclass
# Intermediate class
class Mother(grandMotherclass.Grandmother):
    def __init__(self, mothername, grandmothername):
        self.mothername = mothername
 
        # invoking constructor of Grandmother class
        grandMotherclass.Grandmother.__init__(self, grandmothername)