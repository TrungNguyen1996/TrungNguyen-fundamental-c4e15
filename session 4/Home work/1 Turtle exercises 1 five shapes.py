from turtle import *

#  Vẽ tam giác 3 cạnh
color("red")
for i in range(3):
    forward(50)
    left(120)

# Vẽ hình vuông 4 cạnh màu lam
color("blue")
for i in range(4):
    forward(50)
    left(90)

#  Vé hình ngũ giác 5 cạnh màu nâu
color("brown")
for i in range(5):
    forward(50)
    left(72)


#  Vé hình lục giác 6 cạnh màu vàng
color("yellow")
for i in range(6):
    forward(50)
    left(60)

#  Vé hình thập giác 6 cạnh màu xám
color("grey")
for i in range(7):
    forward(50)
    left(51.428571428)
print("tam giác, vuông, ngũ giác, lục giác, thập giác")
mainloop()
