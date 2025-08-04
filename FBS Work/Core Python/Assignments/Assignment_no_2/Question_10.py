
## Write a program to reverse three-digit number.

num = int(input("Enter the three digit no.: "))

hun = num // 100

ten = (num // 10)%10

unit = num % 10

a= hun * 1
b = ten * 10
c = unit *100
sum = a+b+c
print(f"{sum}")