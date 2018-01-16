from turtle import *

# color("firebrick")
color("red")
for i in range(4):

    left (30)
    forward(150)
    # Rẽ hướng rồi tiến để xoay hướng tạo hình thanh bông hoa, vì
    # cạnh ấy phải thay đôi không theo trục chính

    right (60)
    forward(150)

    right (120)
    forward(150)

    left(120)
    backward(150)
    right(60)
    #  LÙI lại rẽ sang phần phải của Hướng mặc đinh trái sáng phải
left(120)
left(360)

print("Hoa dep")

mainloop()
# vòng lặp chính
