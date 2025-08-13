
## Enter number of students from user. For those many students accept marks of 5
## subject marks from user and calculate percentage. Display all percentage and
## average percentage of students.

num_student = int(input("Enter the number of student: "))
total_per = 0

for i in range (1, num_student+1):
    print(f"student{i}")
    total_marks = 0

    for i in range(1, 6):
        marks = int(input(f"Enter the marks:"))
        total_marks += marks

    per = total_marks/5
    print(f"Percentage{per}%")

    total_per += per

average_per = total_per/num_student
print(f"Average percentage of all student is {average_per}%")        