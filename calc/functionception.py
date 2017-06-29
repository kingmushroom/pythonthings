def addFactory(type):
    if(type==1):
        def add(a,b):
            return a+b
        return add
    else:
        def add(a,b):
            return a*b
        return add

def runFunction(func):    
    print(func(1,2))
    
b=addFactory(1)(4,5)
c=addFactory(5)(9,9)
d=lambda a,b:a*b #testing lambda function, does a similar thing to the addfactory
print(b)
print(c)
print(d(9,9))
runFunction(d)
