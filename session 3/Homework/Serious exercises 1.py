# # Exercise 1: Write a program to check whether a number is a prime number
# TIẾNG VIỆT
# # Viết một chương trình để kiểm tra xem một số là một số nguyên tố
# Kiem tra so dau vao 
def KierTraDauVao():
    while Ture:
    number = int(("nhap sp :"))
    if number == 2 :
        print '- So', number,' la so nguyen to!'
        break
    elif number == 1 :
        break
    elif number < 0 :
        print '- so nhap vao phai lon hon 1 va la nguyen duong'
        print '--- vui long nhap lai so'
        continue
    else:
        break
    return number
# Kierm tra so nguyen to
def Kiermtrasonguyen(number):
    count = 2
    while True:
    if number == 1:
        print 'so', number, 'khong phai so nguyen to !'
        break

    number_check = number % count

    if count == number:
        print 'so', number, ' la so nguyen to !'
        break

    if number_check  == 0:
        print 'so', number, 'khong phai so nguyen to !'
        break
    else:
        count = count + 1
        continue


