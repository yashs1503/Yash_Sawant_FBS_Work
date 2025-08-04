
## WAP to input angle triangle and check wether triangle is valid or not 

a = int(input("Enter the First Angle: "))
b = int(input("Enter the Second Angle: "))
c = int(input("Enter the Third Angle: "))

if a + b +c == 180:
    print(f'{a},{b},{c} are a triangle')

else:
    print(f"{a}{b}{c} are a not a triangle ")