oneString,twoString,outputOne,outputTwo,vowels = "QA Consulting","Office for National Statistics","","",("A","E","I","O","U")
for x in oneString:    
    if x.upper() in vowels:        outputOne=outputOne+x
for x in twoString:    
    if not(x.upper() in vowels):        outputTwo=outputTwo+x       
print(outputOne,"\n",outputTwo)
#outputThree = outputOne.center(500,"M")
#print(outputThree)
