
## Write a program to enter P, T, R and calculate simple Interest.

p = int(input("Enter the Principle Amount: "))
t = int(input("Enter the time: "))
r = int(input("Enter the rate of percentage: "))

res = (p*r*t/100)
print(f"""The simple interest of principle amount {p} Rs for the time of {t} years
      and rate of percentage {r} % is {res}""")