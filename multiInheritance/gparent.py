class grandparent():
    
    def swim(self):
        print("Grandparent swim method")
        #super.swim()
class parentOne(grandparent):
    def swim(self):
        print("Parentone swimmethod")
        #super().swim()
class parentTwo(grandparent):
    def swim(self):
        print("Parent two swim method")
        #super().swim()
        
class parentThree(grandparent):
    def swim(self):
        print("Parent three swim method")
        #super().swim()

class child(parentTwo,parentThree,parentOne,grandparent):
    def swimt(self):
        print("Child swim method")
        super(parentThree,self).swim()
        
        
bob=child();
#bob.swim()
bob.swimt()
super(parentThree,parentThree()).swim()
parentThree.swim(parentThree())

#marie=super(child,self).swim()
