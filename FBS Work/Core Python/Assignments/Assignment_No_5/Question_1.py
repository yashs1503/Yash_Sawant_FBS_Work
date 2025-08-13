
## Write a program to prompt user to enter userid and password. If Id and
## password is incorrect give him chance to re-enter the credentials. Let him try 3
## times. After that program to terminate.

id = "yash"
password = 2003

for i in range (3):
    user_id = input("Enter the user id: ")
    user_pass = int(input("Enter the user password: "))

    if id == user_id and password == user_pass:
        print("Login Successful..")
       
    else:
        print("Invalid credentials, try again.. ")
else:
    print(" Faild Attempts.")