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

