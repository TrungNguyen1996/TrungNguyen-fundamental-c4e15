count = 0
# dieu kien ban dau
while count < 5:
        # dieu kien de vong lap con chay
        yob = int(input("Your name fo birth"))
        age = 2018 - yob

        if yob < 10:
             print("Baby")
        elif age < 18:
            print ("Teenager")
        else:
            print ("Adult")
    # dieu kien de co su thay doi

        count += 1
        if count >= 5:
            break
#  typerace go nhanh
#  cau lenh nao cung ket thuc baawng dau hai cham
#  Ctrl C buoc tr ch pahi tat, hoac ctrl c
#  break va contuniue pha vong lap gan no nhat cho tat ca cac vong lap

#        Hoi

#  chi nen gioi quyet mot van de cua mot thoi diem
