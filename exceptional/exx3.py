#Chocolate?
def sum(a,b):
    c=a+b;raise "Mike"
    print("%d + %d = %d"%(a,b,c))
    return c

try:
    assert sum(1,2)==3,"Bad maths, should be 3"
except:
    print("The maths is wrong")
    print("get it right")
finally:
    print("Maths is fun")
    
#what will print