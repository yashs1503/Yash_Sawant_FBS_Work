
## Write a program to calculate the percentage of student based on marks of any 5
##subjects.

m1 = int(input("Enter the m1 marks:"))
m2 = int(input("Enter the m2 marks:"))
m3 = int(input("Enter the m3 marks:"))
m4 = int(input("Enter the m4 marks:"))
m5 = int(input("Enter the m5 marks:"))

total_marks = m1+m2+m3+m4+m5
per = (total_marks/500*100)
print(f"percentage of best five marks {per} %")
