
## Write a program to check if user has entered correct userid and password.


u_id = input("Enter the User Id: ")
u_pass = int(input("Enter the User Password: "))

a_id = "Admin"
a_pass = 2003


if (u_id==a_id and u_pass==a_pass):
    print("User_id And User_pass is Correct")

else:
    print("Use_id and user_pass is Not Correct")


    