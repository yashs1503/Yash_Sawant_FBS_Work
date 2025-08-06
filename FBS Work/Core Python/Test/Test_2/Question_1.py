

## Write a program to accept year from user and check if it is a leap year or not.

year = int(input("Enter tye year: "))

if year % 4 == 0:
    if year % 100 == 0:
         if year % 400 == 0:
              print(f"{year} is a leap year.")

         else:
              print(f'{year} is a not a leap year.')
    else:
         print(f"{year} is a leap year.")
else:
     print(f"{year} is a not leap year.") 