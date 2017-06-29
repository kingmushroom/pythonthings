from scipy.constants.codata import physical_constants
class Student:
    def __init__(self,phy=0,che=0,mat=0):
        self.__phy=phy
        self.__che=che
        self.__mat=mat
   
    def __add__(self,r):
        bob=Student()
        bob.physics(self.__phy+r.physGet())
        bob.maths(self.__mat+r.matGet())
        bob.chemistry(self.__che+r.cheGet())
        return bob
    
    def __sub__(self,r):
        bob=Student()
        bob.physics(self.__phy-r.physGet())
        bob.maths(self.__mat-r.matGet())
        bob.chemistry(self.__che-r.cheGet())
        return bob
    
    def __mul__(self,r):
        bob=Student()
        bob.physics(self.__phy*r.physGet())
        bob.maths(self.__mat*r.matGet())
        bob.chemistry(self.__che*r.cheGet())
        return bob
    
    def __truediv__(self,r):
        bob=Student()
        print("Real men don't divide")
        return bob
    
    def __str__(self):
        output=""
        output+= "Physics Mark:"+str(self.physGet())+"\n"
        output+="Maths Mark:"+str(self.matGet())+"\n"
        output+="Chemistry Mark:"+str(self.cheGet())+"\n"
        return output
        
    def matGet(self):
        return self.__mat
    def cheGet(self):
        return self.__che 
    def physGet(self):
        return self.__phy    
    def physics(self,p):
        if(p in range(0,150)):
            self.__phy=p
    def chemistry(self,c):
        if(c in range(0,150)):
            self.__che=c
    def maths(self,m):
        if(m in range(0,150)):
            self.__mat=m
            
    def calcResults(self):
        self.__total=(self.__phy+self.__che+self.__mat)
        self.__per=(self.__total/450)*100
        print(self.__total, self.__per)
    def returnAnswer(self):
        x=self.__per
        if(self.__per<70):
            print("Fool")