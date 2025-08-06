
## Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.

height = int(input("Enter the Height: "))
weidth = int(input("Enter the Weigth: "))
cost = int(input("Enter the cost of paint: "))

a_wall = height * weidth
total_a_wall = a_wall * 4

cost = total_a_wall * cost

print(f"Total cost of painting is {cost}.")