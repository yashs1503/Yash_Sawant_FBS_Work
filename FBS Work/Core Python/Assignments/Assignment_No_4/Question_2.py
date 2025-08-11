
## WAP to print all odd numbers until n.
n = int(input("Enter the number.: "))

for n in range (n + 1):
    if n % 2 != 0:
        print(n)