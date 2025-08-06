
## A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

pro_1 = int(input("Enter the product 1 Price: "))
pro_2 = int(input("Enter the product 2 Price: "))
pro_3 = int(input("Enter the product 3 Price: "))
pro_4 = int(input("Enter the product 4 Price: "))
pro_5 = int(input("Enter the product 5 Price: "))

total_prise = pro_1 + pro_2 + pro_3 + pro_4 + pro_5

bill = total_prise * 0.18

print(f"The total bill After adding GST is:{bill} ")