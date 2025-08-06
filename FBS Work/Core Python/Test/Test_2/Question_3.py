
## A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
## for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
## length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
## cost of fencing the field.

r = 20
l = 50
b = 40 
cost = 35 
round = 5

cir_per = 3.14 * r
rec = l + 2 * b

total_per = cir_per + rec

total_len = total_per * 5

total_cost = total_len * cost

print (f"Total Cost of fencing the feild is {total_cost}")