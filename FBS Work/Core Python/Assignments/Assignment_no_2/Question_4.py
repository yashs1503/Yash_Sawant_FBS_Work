
## WAP to calculate area of triangle and rectangle

base = int(input("Enter the base of triangle: "))
hight = int(input("Enter the hight of triangle: "))
 
a_tri = 0.5*base*hight

print(f"Area of triangle is {a_tri}")

length = int(input("Enter the length of rectangle: "))
breadth = int(input("Enter the breadth of rectangle : "))

a_rec = length*breadth

print(f"Area of rectangle is {a_rec}")

print(f"Area of triangle is {a_tri} and area of rectangle is {a_rec}")