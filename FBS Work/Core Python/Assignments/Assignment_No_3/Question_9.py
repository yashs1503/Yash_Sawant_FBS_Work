
## Input 5 subject marks from user and display grade(eg.First class,Second class ..)

s1= int(input("Enter the First Sub Marks: "))
s2= int(input("Enter the Second Sub Marks: "))
s3= int(input("Enter the Third Sub Marks: "))
s4= int(input("Enter the Fourth Sub Marks: "))
s5= int(input("Enter the Fifth Sub Marks: "))

total_marks=s1+s2+s3+s4+s5
per = ((total_marks/500)*100)
print(f"Percentage is {per}")

if (per>=91):
    print(" A+ Grade")

elif (per>=81):
    print(" A Grade")

elif (per>=71):
    print(" B Grade")

elif (per>=61):
    print(" C Grade")

else:
    print("Pass")

