def getDigits(num):
    thisnumSize=str(num).__len__()
    modNum = "1"+str((thisnumSize-1)*"0")
    thisDig = int((num-(num%int(modNum)))/int(modNum))
    smallmod=int(modNum)/10
    num=num-(thisDig*int(modNum))
    thisnumSize=str(num).__len__()
    return thisDig,num,thisnumSize
def printDigits(number):
    dig,number,dignum=getDigits(number)
    wenthere=False
    if(dignum>2):
        print("%s thousand"%ones[dig],end=" ")
        dig,number,dignum=getDigits(number)
        wenthere=True
    if(dignum>2):
        print("%s hundred"%ones[dig],end=" ") if(dig>0) else print("and",end=" ")
        dig,number,dignum=getDigits(number)    
    if(dignum>1):
        print("and %d"%teens[number],end=" ") if(dig==1) else print("and %s"%tens[dig],end=" ")
        dig,number,dignum=getDigits(number)
    if(dignum==1):
        if(wenthere): print("and",end=" ")
        print(ones[dig])      
ones,teens,tens,number,forthdig,thirddig,secondDig,firstDig={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"},{10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"},{2:"twenty",3:"thirty",4:"fourty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"},int(input("What number would you like?")),-1,-1,-1,-1
printDigits(number)