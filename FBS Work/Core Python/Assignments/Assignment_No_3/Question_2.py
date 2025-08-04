
## Write a program to input any alphabet and check weather it is vowel or consonant

a = input("Enter the alphabet: ")

##if a == a or a == A or a == e or a == E or a == i or a == I or a == o or a== O or a == u or a == U :
  ##  print(f"{a} is Vowel")
if (a in 'aeiouAEIOU'):
    print(f"{a} is Vowel")

else:
    print(f'{a} is a Consonant ')