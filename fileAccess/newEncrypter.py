msg = "Mike is the mikest mike of all the mikes"
output=""
counter=0
for x in msg:
    output=output+(ord(x)*"-")+"/"
print(output)
letters = output.split("/")
decrypted=""
for let in letters:
    counter=0
    for l in let:
        
        if l is "-":
            counter=counter+1
    character=chr(counter)
    decrypted=decrypted+character
        
print(decrypted)