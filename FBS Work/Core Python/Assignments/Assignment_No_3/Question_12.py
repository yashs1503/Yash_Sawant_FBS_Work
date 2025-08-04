
##Write a program to check if given 3 digit number is a palindrome or not.

a = int(input("Enter the Three digit No.: "))

d1= a//100

d2= (a//10)%10

d3= a%10
rev= (d3*100)+(d2*10)+d1
print(f"{rev}")

if a == rev:
    print("No. is Palindrome")
else:
    print("No. is Not Palindrome")
