# bai seach
print('''
Hi there,
Thinh about a number form 0 to 100, then press ENNTER
''')

lo = 0
hi = 100
loop = True
while loop:
    mid = (lo + hi) // 2 # // la ra so nguyen printprint
    answer = input("Is {0} your number".format(mid))
  # answer = input("Is" + str(mid) + "your number")
    if answer.lower() == 'c' : # luôn đúng: bọc c thành chữ thường
        print("I new it")
        loop = False # vòng 1 này làm vòng lặp thoát dc
    elif answer.lower() == 's':
        hi = mid
    elif answer.lower() == 'l':  # chuyen s tring (ki tu) thanh so thuong
        lo = mid

#
