# n = int(input(" 1*2*3*...*n "))
#
# for i in range (0, n-1):
#     n = n * (i+1)
#
# print ("Ket qua '1*2*3*...*n' la: ", n)

n = int (input("moi ban nhap vao so" ))

sum = 1 # dk dau

for i in range(1, n + 1 ):
    # print(sum)
    sum *= i
print(sum)

# bài anh Huy hướng dẫn chữa 17 01 2018
