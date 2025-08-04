
## Calculate the cost of painting the following building’s walls (both interior and
## exterior). You need to accept area (one wall) and cost of both interior and
## exterior wall.
## (Note: 1. Below diagram is of two joint rooms.
## 2. It is upper view of building.)

w_area = int(input("Enter the area of one wall: "))
int_cost = int(input("Enter cost of area for interior wall: "))
ext_cost = int(input("Enter cost of area for exterior wall: "))

total_wall = 8
shared_wall = 1
ext_wall = total_wall - shared_wall

total_int_area = total_wall * w_area
total_ext_area = ext_wall * w_area

total_int_cost = total_int_area * int_cost
total_ext_cost = total_ext_area * ext_cost

total_cost = total_int_cost + total_ext_cost
print("      ")
print(f"Total interior wall area: {total_int_area}")
print(f"Total exterior wall area: {total_ext_area}")
print(f"Interior painting cost: {total_int_cost}")
print(f"Exterior painting cost: {total_ext_cost}")
print(f"Total painting cost: {total_cost}")
