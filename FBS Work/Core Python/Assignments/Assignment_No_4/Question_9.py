
## WAP to print all numbers in a range divisible by a given number.
num = int(input("Enter the Number: "))
n = int(input("Enter range of divisible the Number: "))

for n in range (1 ,n+1):
    if n % num ==0:
        print(n)