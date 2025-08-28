
### 1. Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1)
    
def sum_ser(num):
    if num == 0:
        return 0
    else:
        return fact(num) +sum_ser(num-1)
    
num = int(input("Enter the number: "))
fact = sum_ser(num)
print(fact)