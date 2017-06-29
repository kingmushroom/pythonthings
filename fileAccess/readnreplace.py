#fileData=open(input('Enter filename: '),"r").read()
#theFile=open(input('Enter destination: '),"w")
fileData,theFile,find,replace = open(input('Enter filename: '),"r").read(),open(input('Enter destination: '),"w"),input('Find what?: '),input('Replace with?: ')
for Chr in fileData:    fileData=theFile.write(replace) if Chr is find else (theFile.write(Chr))
#theFile.close()        


