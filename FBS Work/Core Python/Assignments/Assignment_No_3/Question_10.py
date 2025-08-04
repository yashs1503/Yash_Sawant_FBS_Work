
## Write a program to check if person is eligible to marry or not (male age >=21 and
## female age>=18)

gender = input("Enter the gender Male/Female: ")
age = int(input("Ente the Age: "))

if gender=="M" and age>=21 or gender=="F" and age>=18:
    print("Eligible for Marriage")
else:
    print("Not Eligible for Marriage")