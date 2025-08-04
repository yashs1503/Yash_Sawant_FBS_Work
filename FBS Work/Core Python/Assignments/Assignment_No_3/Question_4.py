
## Write a program to input all sides of a triangle and check whether triangle is valid or
## not.

a = int(input("Enter the First side: "))
b = int(input("Enter the Second side: "))
c = int(input("Enter the Third side: "))

if (a + b > c) and (a + c > b) and (c + b > a):
    print( " This is a Triangle " )

else:
    print("This is a not a Triangle")