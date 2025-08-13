
## Accept no. of passengers from user and per ticket cost. Then accept age of each
## passenger and then calculate total amount to ticket to travel for all of them based on
## following condition :
## a. Children below 12 = 30% discount
## b. Senior citizen (above 59) = 50% discount
## c. Others need to pay full.

no_passenger = int(input("Enter the no, of passengers: "))
cost_ticket = int(input("Enter the cost of ticket: "))
total_cost = 0

for i in range (1, no_passenger+1):
    age = int(input(f"Enter the age{i}: "))
    
    if age < 12:
        cost = cost_ticket * 0.7
    elif age > 59:
        cost = cost_ticket * 0.5
    else:
        cost = cost_ticket

    print(f"ticket cost of {i} passenger {cost}")
    total_cost += cost

print(f"Total cost of passenger is {total_cost}")