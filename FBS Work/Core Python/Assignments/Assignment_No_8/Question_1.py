
# 1. Write a program to calculate area of rectangle

def area_rectangle(l,w ):
    return l*w

length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))

area = area_rectangle(length,width)
print(f"Area of Retangle is {area}")