
## WAP to calculate total salary of employee based on basic, da=10% of basic,
## ta=12% of basic, hra=15% of basic.

salary = int(input("Enter the amount of salary: "))

da = (salary*10)/100
ta = (salary*12)/100
hrs = (salary*15)/100

total = salary+da+ta+hrs
print(f"The total salary of Employee is {total}")
