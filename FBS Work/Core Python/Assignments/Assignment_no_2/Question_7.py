
## Find the sum of three-digit number.

a = int(input("Enter the three digit no: "))
temp = a

d1 = temp % 10
temp = temp//10

d2 = temp % 10
temp = temp//10

d3 = temp % 10
temp = temp//10

print(f"the unit no is: {d1}\ntens no is: {d2}\nhunderd no is: {d3}")

sum = d1+d2+d3
print(f"Sum of three digit no.: {sum}")