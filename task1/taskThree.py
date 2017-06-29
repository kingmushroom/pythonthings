sal=int(input("Enter Salary:"))
gra=input("Enter Grade:")
dept=input("Enter dept:")
rate,taxableSal=0,0
print("Salary is £%d\nGrade = %s\nDept = %s" %(sal,gra,dept))
if sal>15000:
    if dept.upper() == 'IT':
        if (type(gra) is str) and (gra.upper() is "CTO"): rate=2
        elif type(gra)is int and (int(gra) is range(1,11)): rate=9
        else: rate=15
    elif dept.upper() == "HR":
        if (type(gra) is str) and (gra.upper() is "CTO"): rate=0
        if type(gra)is int and (int(gra) is range(1,11)): rate=9
        else: rate=17
    taxableSal=(sal-15000)*(rate/100)
if dept.upper() == 'IT':
    print("Bonus is: £",sal*(5/100))
    sal=sal+(sal*(5/100))
print("Tax rate is %d%% is £%d\nFinal pay equals £%d" %(rate,taxableSal,(sal-taxableSal)))

        
