fileData,theFile,find,replace,newfile,counter = open(input('Enter filename: '),"r").read(),open(input('Enter destination: '),"w"),input('Find what?: '),input('Replace with?: '),"",0
findSize=find.__len__()
while True:
    if fileData.find(find)>-1: 
        for x in range(counter,fileData.find(find)):
            newfile=newfile+fileData[x]
        newfile=newfile+replace
        fileData=fileData[fileData.find(find)+findSize:]
        counter=+findSize
    else:
        newfile=newfile+fileData
        break
print(newfile)
theFile.write(newfile)
    
#else: #(theFile.write(Chr))