from character import Character
from test._test_multiprocessing import msvcrt

w,h=30,10
theMap=[['"' for x in range(w)] for y in range(h)]
for a in range(10):
    theMap[a][29]="\n"

characters=[]

characters.append(Character('Mike',8,28,"@"))
characters.append(Character('Bob',2,8,"O"))

#print(mike.getHealth())
#mike.getHurt(20)
#print(mike.getHealth())
#print(bob.getHealth())
#print(mike.getName())
#mike.hit(bob)
#print(bob.getHealth())
mainChar=""
for char in characters:
    if(char.name is'Mike'):mainChar=char
    theMap[char.xpos][char.ypos]=char.model
    

##print(theMap[1][9])
print(theMap)

def drawScreen():
    x=0
    w,h=30,10
    theMap=[['"' for x in range(w)] for y in range(h)]
    for a in range(10):
        theMap[a][29]="\n"
    for char in characters:
        mainChar=char
        theMap[char.xpos][char.ypos]=char.model
    for x in range(10):
        for a in theMap[x]:
            print(a,end=" ")
        x+=1
        
drawScreen()

while(True):
    inp=input("which way? u,d,l or r")
    
    if(inp is "l"):
        mainChar.move(0,-1,characters)
    if(inp is "r"):
        mainChar.move(0,1,characters)
    if(inp is "d"):
        mainChar.move(1,0,characters)
    if(inp is "u"):
        mainChar.move(-1,0,characters)
    drawScreen()