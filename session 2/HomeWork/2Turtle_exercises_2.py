from turtle import *

#  Vẽ tam giác 3 cạnh
color("blue")
for i in range(3):
    forward(50)
    left(120)

# Vẽ hình vuông 4 cạnh màu đỏ
color("red")
for i in range(4):
    forward(50)
    left(90)

#  Vé hình ngũ giác 5 cạnh màu lục
color("blue")
for i in range(5):
    forward(50)
    left(72)


#  Vé hình lục giác 6 cạnh màu lục
color("red")
for i in range(6):
    forward(50)
    left(60)

print("tam giác, vuông, ngũ giác, lục giác")
mainloop()

#  Ý tưởng của bài là mũi tên sẽ chạy 1 vòng hết 360 độ và dùng 360 chia cho số góc kề của mỗi hình để tính ra góc xoay đúng
#  và lưu ý là  Tại hướng MẶC ĐỊNH chuyển tiến TRƯỚC rồi mới rẽ ạ
#  HƯỚng Tuấn theo của mũi tên là trái sáng phải khi nhìn màn hinh ạ
