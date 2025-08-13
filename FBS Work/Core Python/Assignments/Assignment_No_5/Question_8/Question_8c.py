
## c. Find the sum of a geometric series from 1 to n where the common ratio is 2.  

n = int(input("Enter n: "))
sum = 0
for i in range(n):
    sum += 2 ** i 
print(f"The sum of the geometric series from 1 to {n} with a common ratio of 2 is: {sum}")
