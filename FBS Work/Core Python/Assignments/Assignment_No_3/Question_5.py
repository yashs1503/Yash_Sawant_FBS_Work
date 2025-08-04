

## Write a program to check whether the triangle is equilateral, isosceles or scalene
## triangle.

a = int(input("Enter the First Angle: "))
b = int(input("Enter the Second Angle: "))
c = int(input("Enter the Third Angle: "))
if (a==b) and (b==c):
    print("Triangle is Equilateral")
elif( a==b ) or (b==c) or (a==c):
    print("Triangle is Isosceles")
else:
    print("Triangle is Scaler")
    
    



    
