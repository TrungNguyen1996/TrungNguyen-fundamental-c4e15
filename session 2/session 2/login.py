# print("Hello all, this is a super autogetway")
# x = input("Usename: ")
# y = input("Password: ")
#
# if x == "c4e":
#     if y == "codethechange":
#         print("Welcom,", x)
#     else:
#         print("Your Password is wrong")
#
# else:
#     print("You are not superuse")

# de khong thay pass thif tim python 3 input witho

from getpass import getpass
print("welcome to superuser gateway")
att = 0
while att <=3:
    att +=1
    username = input("Username: ")
    if username == "admin":
        password = getpass("Password: ")
        if password == "blahblah":
            print("Welcome ",username)
            break
        else:
            print("Wrong password!!")
    else:
        print("User does not exist!!")
