
## 2. Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.

num = int(input("Enter the three digit no.: "))

f_no = num // 100
s_no = (num//10)%10
t_no = num % 10

if f_no == 2 * s_no and f_no == t_no / 2:
    print("Yes, you have done it")

else:
    print("Please try next time")