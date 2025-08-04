
## Write a program to enter P, T, R and calculate Compound Interest.

p = int(input("Enter the Principle Amount: "))
t = int(input("Enter the time: "))
r = int(input("Enter the rate of percentage: "))

res = (p*(1+r/100)**t)

ci = res - p

print(f"""The Compound interest of principle amount {p} Rs for the time of {t} years
      and rate of percentage {r} % is {ci}""")