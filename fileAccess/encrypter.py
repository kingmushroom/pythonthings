fileData,theFile= open(input('Enter filename: '),"r").read(),open(input('Enter destination: '),"w")
thisTable,outTable=("abcdefghijklmnopqrstuvwxyz"),("zyxwvutsrqponmlkjihgfedcba")
theFile.write(fileData.translate(str.maketrans(thisTable,outTable)))

