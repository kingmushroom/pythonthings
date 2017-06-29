sentence,alphabetArr=input("Input sentence"),{}
for a in sentence:
    if(a in alphabetArr):        alphabetArr[a]=alphabetArr[a]+1
    else:
        if(ord(a)<97):a=chr(ord(a)+32)
        alphabetArr.__setitem__(a, 1)
print(alphabetArr)
#for a in alphabetArr:
 #   if(alphabetArr[a]>0):        print(a," - ",alphabetArr[a])