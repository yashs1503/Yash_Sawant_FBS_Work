
## WAP to calculate selling price of book based on cost price and discount.

cp = int(input("Enter the cost prise: "))
d = int(input("Enter the discount: "))

dp = cp*10/100  # dp = discount price

sp = cp + dp  

print(f"Selling prise is {sp}")