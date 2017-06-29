def add(a):
    print("Result is %d" %(int(a[0])+int(a[1])))
    if(repeat()):
        add(inputNums())
    else:
        mainLoop()
def inputNums():
    a=[]
    while True:
        a.append(input('Enter first number: '))
        a.append(input('Enter second number: '))
        if not(a[0].isalpha())or(a[1].isalpha()):
            break
        else:
            print("must be numbers, berk")
    return a
def sub(a):
    print("Result is %d" %(int(a[0])+int(a[1])))
    if(repeat()):
        sub(inputNums())
    else:
        mainLoop()
def mul(a):
    print("Result is %d" %(int(a[0])*int(a[1])))
    if(repeat()):
        mul(inputNums())
    else:
        mainLoop()      
def div(a):
    if(int(a[1])<1):
        print("No Dividing by zero")
        div(inputNums())
    else:
        answer=float(a[0])/float(a[1])
        print("Result is %f" %(answer))
        if(repeat()):
            div(inputNums())
        else:
            mainLoop()
def repeat():
    while True:
        choice = input('Repeat process y or n: ')
        if(choice is "y"):
            output=True
            break
        elif(choice is "n"):
            output=False
            break
        else:
            print("choose one of the two options")
    return output 
def tim():
    number = int(input('Input number: '))
    for x in range(1,11): 
        ans=x*number
        if x<10:
            x=" "+ str(x) 
        if ans<10:
            ans=" "+ str(ans)  
        print(x,"x",number,"=",ans)
    if(repeat()):
        tim()
    else:
        mainLoop()
def mainLoop():
    print("Select option\n1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n5 - Times Table\n6 - Quit")
    Choice = input('Enter your choice: ')
   # switches={1:add(inputNums()),2:sub(inputNums()),3:mul(inputNums()),4:div(inputNums()),5:tim(),6:quit()}
   # switches.get(Choice)
    if Choice.isalpha() or int(Choice)>6:
        print("You must choose a number between 1 and 6")
    elif Choice is "1":
        add(inputNums())
    elif Choice is "2":
        sub(inputNums())  
    elif Choice is "3":
        mul(inputNums()) 
    elif Choice is "4":
        div(inputNums()) 
    elif Choice is "5":
        tim() 
    elif Choice is "6":
        quit
mainLoop()
