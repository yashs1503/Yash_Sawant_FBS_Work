
## Write a program to swap two numbers using third variable.

x = int(input("Enter the x value: "))
y = int(input("Enter the y valuve: "))

z = x
x = y 
y = z

print(f"y value is store in x={x} and x value is store in y={y}")
