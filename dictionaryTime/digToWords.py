ones,teens,tens,number,forthdig,thirddig,secondDig,firstDig={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"},{10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"},{2:"twenty",3:"thirty",4:"fourty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"},int(input("What number would you like?")),-1,-1,-1,-1
def getDigits(num):    thisnumSize=str(num).__len__();    modNum = "1"+str((thisnumSize-1)*"0");    thisDig,num = int((num-(num%int(modNum)))/int(modNum)),num%int(modNum);    return thisDig,num
if(str(number).__len__()==4):    forthdig,number=getDigits(number);     
if(str(number).__len__()==3):    thirddig,number=getDigits(number)    
if(str(number).__len__()==2):    secondDig,number=getDigits(number)
if(str(number).__len__()==1):    firstDig=number
if(forthdig>-1):  
    print("%s thousand"%ones[forthdig],end=" ")
    if((secondDig>0 or firstDig>0)and(thirddig<0)): print("and",end=" ")
if(thirddig>-1):
    print("%s hundred"%ones[thirddig],end=" ")
    if(secondDig>-1 or firstDig>-1): print("and",end=" ")
if(secondDig==1):    print(teens[int(str(secondDig)+str(firstDig))])
else:     print(tens[int(secondDig)],end=" ") if(secondDig>0) else print(ones[firstDig]) 
