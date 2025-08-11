
## WAP to print all integers upto n that aren’t divisible by 2 and 3.
n = int(input("Enter the number: "))

for n in range (n):
    if n % 2 == 0 and n % 3 == 0:
        print(n)