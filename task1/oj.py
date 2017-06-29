class Mike:
    statNumber = 0
    
    def __init__(self,name,time):
        self.name=name
        self.time=time
        Mike.statNumber=+1
        
    def sayTime(self):
        print(self.time)
        
bob = Mike("Mike",1234)
bob.sayTime()
print(Mike.statNumber)
bob2 = Mike("NotMike",6666)

bob3 = Mike("NotasdMike",66566)
print(Mike.statNumber)