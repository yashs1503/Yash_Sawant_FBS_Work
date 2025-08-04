
## Accept age of five people and also per person ticket amount and then calculate total
## amount to ticket to travel for all of them based on following condition :
## a. Children below 12 = 30% discount
## b. Senior citizen (above 59) = 50% discount
## c. Others need to pay full.

age1 = int(input("Enter the Age of Person 1: "))
age2 = int(input("Enter the Age of Person 2: "))
age3 = int(input("Enter the Age of Person 3: "))
age4 = int(input("Enter the Age of Person 4: "))
age5 = int(input("Enter the Age of Person 5: "))

tic_amt= int(input("Enter the Ticket Amount: "))

if age1 < 12:
    dis_amt = tic_amt*0.3
    amt1 = tic_amt - dis_amt
elif age1 >59:
    dis_amt = tic_amt*0.5
    amt1 = tic_amt - dis_amt
else:
    amt1 = tic_amt

if age2 < 12:
    dis_amt = tic_amt*0.3
    amt2 = tic_amt - dis_amt
elif age2 >59:
    dis_amt = tic_amt*0.5
    amt2 = tic_amt - dis_amt
else:
    amt2 = tic_amt

if age3 < 12:
    dis_amt = tic_amt*0.3
    amt3 = tic_amt - dis_amt
elif age3 >59:
    dis_amt = tic_amt*0.5
    amt3 = tic_amt - dis_amt
else:
    amt3 = tic_amt

if age4 < 12:
    dis_amt = tic_amt*0.3
    amt4 = tic_amt - dis_amt
elif age4 >59:
    dis_amt = tic_amt*0.5
    amt4 = tic_amt - dis_amt
else:
    amt4 = tic_amt

if age5 < 12:
    dis_amt = tic_amt*0.3
    amt5 = tic_amt - dis_amt
elif age5 >59:
    dis_amt = tic_amt*0.5
    amt5 = tic_amt - dis_amt
else:
    amt5 = tic_amt

total_amt = amt1+amt2+amt3+amt4+amt5

print(total_amt)