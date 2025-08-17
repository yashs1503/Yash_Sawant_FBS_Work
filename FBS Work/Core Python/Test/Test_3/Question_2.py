# 2. Write a program to calculate the sum of following series
# where n is input by user.
# 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!

n = int(input("Enter the number: "))
total_sum = 0
total_sequence = 0
for i in range(1,n + 1):
    fact = 1
    
    for j in range(1, i + 1):
        fact = fact * j
    
    total_sum = i / fact
    total_sequence += total_sum
   
print(f"Total sum of series is {total_sequence}")