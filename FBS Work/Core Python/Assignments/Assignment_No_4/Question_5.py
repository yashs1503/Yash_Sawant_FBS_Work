
##WAP to print Fibonacci series upto n.

num= int(input("Enter the number: "))
a= -1
b= 1 
for i in range (a, num):
    c=a+b
    print (c)
    a=b
    b=c