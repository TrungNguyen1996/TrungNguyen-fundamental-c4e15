<<<<<<< HEAD
# Exercise 2: Modify the username password in previous session to allow users login at maximum 3 times
# TIẾNG VIỆT
# Sửa đổi mật khẩu người dùng trong phiên trước đó để cho phép người dùng đăng nhập tối đa 3 lần

number = int(input("Enter a number:"))
if number == 2:
    print(number, "is a prime number")
elif number < 2:
    print(number, "is not a prime number")
else:
    i = 2
    while i < number:
        if number % i == 0:
            print(number, "is not a prime number")
            break
        i += 1
    else:
        print(number, "is a prime number")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////
#         maX = 100; miN = 0
# print("Think of a number from 0 to 100 & I will guess it")
# print('''If I'm right, type "c"''')
# print('''If my guess is (S)maller than your number, type "s"''')
# print('''If my guess is (G)reater than your number, type "g"''')
# while True:
#
#     ans = input("Is your number {0} ?".format((maX+miN)//2))
#     if ans == "c":
#         print("I knew it!")
#         break
#     elif ans == "g":
#         maX = (maX+miN)//2
#         continue
#     elif ans == "s":
#         miN = (maX+miN)//2
#         continue
#     else:
#         print("I don't understand your input")
#         break
=======
# Exercise 2: Modify the username password in previous session to allow users login at maximum 3 times
# TIẾNG VIỆT
# Sửa đổi mật khẩu người dùng trong phiên trước đó để cho phép người dùng đăng nhập tối đa 3 lần

Hiện e chịu thôi a
print ("Welcome to Log-in")

n = 3
p = 3
while n != 0:
    username = input("Please input username: ")
    if username != "c4e":
        print("Wrong username!")
        n-=1
    else:
        break
if n == 0:
    print ("You enter user wrong 3 times. Go away!!")
else:
    while p!=0:
        pass_word = input("Please input password: ")
        if pass_word != "yay":
            print("Wrong password!")
            p-=1
        else:
            print ("Yay! You can do anything to me")
            break
    else:
        if p ==0:
            print ("You enter wrong pass 3 times. Go away!")
#q

>>>>>>> 8abc8e53cfabba275c0bbc2837ca1fec99c452f2
