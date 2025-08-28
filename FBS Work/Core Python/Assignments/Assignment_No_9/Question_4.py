
### 4. Write a program to find sum of n numbers using recursion.

def sum_series(num):
    if num == 0:
        return 0
    else:
        return num + sum_series(num-1)
    
num = int(input("Enter the number: "))
sum = sum_series(num)
print(sum)