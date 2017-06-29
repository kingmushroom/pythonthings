


class ONS:
    def msg(self):
        print("Mike")
        
    def add(self,*a):
        total=0
        for m in a:
            total+=m
        print(total)
        
mike=ONS()
mike.add(1,2,3)