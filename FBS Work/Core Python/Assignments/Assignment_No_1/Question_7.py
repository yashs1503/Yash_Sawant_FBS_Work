
##Program to Find the Roots of a Quadratic Equation
a= int(input("Enter the value of a: "))

b= int(input("Enter the value of b: "))

c= int(input("Enter the value of c: "))

sq = ((b**2)-(4*a*c))**0.5

res1 = (-b+sq)/2*a
res2 = (-b-sq)/2*a

print(f"result 1 is {res1} and result 2 is {res2}")