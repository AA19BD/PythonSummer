class PartyAnimal:
    x=0
    def __init__(self):
        print("I am constructed")
    def party(self):
        self.x+=1
        print("So far",self.x)
    def __del__(self):#seldom to use
        print("I am destructed",self.x)
        
an=PartyAnimal()
an.party()
an.party()
an=42
print("an contains",an)