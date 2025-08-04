
## Write a program to calculate profit or loss
 
cp = int(input("Enter the Cost Prise: "))
sp = int(input("Enter the Selling Prise: "))

if sp>cp:
    print("It is Profit")

elif sp<cp:
    print("It is Loss")

else:
    print("Not Profit Not Loss")