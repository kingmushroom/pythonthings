import random

class Character(object):
    
    
    def __init__(self, name,xpos,ypos,model):
        self.name = name
        self.health=99
        self.xpos=xpos
        self.ypos=ypos
        self.model=model
    def move(self,xchange,ychange,charArray):
        xpos+=xchange
        ypos+=ychange
        if(checkCollisions(charArray)):
            print("\n"*100)
            self.xpos+=xchange
            self.ypos+=ychange
    def checkCollisions(self,charArray):
        #for char in
        return true  
    def getHurt(self,x):   
        self.health=self.health-x 
    def getName(self):return self.name
    def heal(self,x):
        self.health=+x
        
    def getHealth(self): return self.health
    def hit(self,char):char.getHit()
    def getHit(self):
        amount = random.randrange(1,20)
        self.getHurt(amount)