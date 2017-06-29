from pprint import pprint
def tables(fromt,to):
    counter= -1 if fromt>to else 1
    
    a=[]
     
    for y in range(fromt,to+counter,counter):
        a2=[]
        for x in range(1,11):    
            z=y   
                #print(x,"x",y,"=",x*y)
            ans=int(x)*int(y)
            if x<10:
                x=str(x).center(1) 
            if int(y)<10:
                z=str(y).center(2)
            if int(ans)<10:
                
                ans=str(ans).center(2)  
            toArray=str(x)+"x"+str(z)+"="+str(ans)
            #pointOne=y-fromt
            a2.append(toArray)
        a.append(a2)
    #pprint(a)
    outPut=""
    x=0
   # print(a[1,1])
     
    for thisa in a:
        print("")
        outPut=""
        for tisx in thisa:
            
            outPut=outPut+" "+str(tisx)
        print(outPut)
        
        
tables(10,2)


#for y in range(10,1,-1):
    #for x in range(1,10):     print(x,"x",y,"=",x*y)

 


