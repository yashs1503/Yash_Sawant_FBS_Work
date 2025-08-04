
## Write a program to accept an integer amount from user and tell minimum
## number of notes needed for representing that amount.

n = int(input("Enter the notes "))
temp = n

t_tho = temp // 2000
temp = temp % 2000

f_hun = temp // 500
temp = temp % 500

tw_tho = temp // 200
temp = temp % 200

hun = temp // 100
temp = temp % 100

fiv = temp // 50
temp = temp % 50

ten = temp // 10
temp = temp % 10


total = t_tho+f_hun+tw_tho+hun+fiv+ten

print(total)
