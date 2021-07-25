class PartyAnimal:
    x=0
    name=""
    def __init__(self,z):
        self.name=z
        print(self.name,'constructed')
        
    def party(self):
        self.x+=1
        print(self.name,"party count",self.x)
    
s=PartyAnimal("Sally")#We have two independent instances.
s.party()

j=PartyAnimal("Jim")#We have two independent instances.
j.party()
s.party()
