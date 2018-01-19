# # Exercise 1: Write a program to check whether a number is a prime number
# TIẾNG VIỆT
# # Viết một chương trình để kiểm tra xem một số là một số nguyên tố
num = int(input("Enter a number: "))


while True:
    if num < 2:
        print("Khong phai so nguyen to")
    for i in range(2,num + 1):
        if num == 2:
            print("So nguyen to")
        elif num % i == 0:
            print("Khong phai so nguyen to")
        else:
            print("So nguyen to")
        break
    break

    y = int(input("Enter your number: "))
x = y // 2

while x > 1:
    if y % x == 0:
        print(y, 'is not a Prime number')
        break
    x -= 1
else:
    print (y, "is a Prime number")
