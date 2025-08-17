# 2. Write a program to calculate area of circle

def are_circle(radius):
    return 3.14* radius*radius

r = int(input("Enter the radius of circle: "))

area = are_circle(r)
print(f"Area of circle is {area}")