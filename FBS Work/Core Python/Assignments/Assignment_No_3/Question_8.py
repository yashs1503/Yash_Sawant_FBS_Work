
## Write a program to prompt user to enter userid and password. After verifying
## userid and password display a 4 digit random number and ask user to enter the
## same. If user enters the same number then show him success message otherwise
## failed. (Something like captcha)

import random
captcha = random.randint(1111, 9999)

u_id = input("Enter the User Id: ")
u_pass = int(input("Enter the User Password: "))
print(captcha) 
cap = int(input("Enter the Captcha"))
a_id = "Admin"
a_pass = 2003


if (u_id==a_id and u_pass==a_pass and captcha==cap ):
    print("Succesfully Login")

else:
    print("Use_id, user_pass and captcha is Not Correct")


