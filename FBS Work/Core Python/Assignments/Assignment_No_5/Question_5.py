
## Write a program to accept an integer amount from user and tell minimum
## number of notes needed for representing that amount. (Use looping to optimize
## the problem)

amount = int(input("Enter the amount: "))

print("Minimun notes: ")

for note in (2000, 500, 200, 100, 50, 20, 10):
    if amount>=note:
        count = amount // note
        amount = amount % note
        print(f"{note} = {count}")