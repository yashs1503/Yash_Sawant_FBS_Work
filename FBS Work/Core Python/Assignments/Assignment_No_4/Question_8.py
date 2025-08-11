
## WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

n = int(input("Enter the numbe: "))

for n in range (n):
    if n % 7 == 0 and n % 5 == 0:
        print(n)