

## Write a program to accept distance in km and convert it into meters and
## centimeters both.

km = int(input("Enter the distance: "))

m = km * 1000
cm = km * 100000

print (f'The distance is {m}m and {cm}cm')