
## Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter the feet: "))
inches = int(input("Enter the inches: "))

total_inc = (feet*12) + inches
total_mi = total_inc * 0.0254

meter = int(total_mi)
re_cm = (total_mi-meter)*100

print(f'Distence is {meter} meter and {re_cm} centimeters')