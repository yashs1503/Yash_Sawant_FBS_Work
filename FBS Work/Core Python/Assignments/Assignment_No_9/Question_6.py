
### 6. Write a program to print Fibonacci series using recursion.

def fib(n, a, b):
    if(n > 0):
        c = a + b
        print(c)
        fib(n - 1, b, c)

num = int(input("Enter the number:"))
a = -1
b = 1
fib(num, a, b)