from student import Student
mike=Student()
mike.physics(100)
mike.chemistry(100)
mike.maths(100)
mike.calcResults()
mike.returnAnswer()
bob=Student(1,1,1)
nigel=bob+mike
mary=nigel-bob
clive=nigel*nigel
bertie=bob/nigel

print(nigel)
print(mary)
print(clive)
print(bertie)