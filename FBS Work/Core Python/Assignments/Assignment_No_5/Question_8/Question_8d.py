
## d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10   

a = int(input("Enter value: "))
total = 0

for i in range(1, 11):          
    term = (a ** i) / i       
    total += term               

print(f"Sum of the series:{total}" )