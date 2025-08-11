
## WAP to check if a given number is prime number or not.
num = int(input("Enter the number.: "))

for i in range (2, num//2):
    if num % i == 0:
        print(f"{num} is a not Prime number.")
        break

else: 
    print(f"{num} is a Prime number.")