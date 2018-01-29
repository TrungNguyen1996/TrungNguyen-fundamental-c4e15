from turtle import *
# 1
begin_fill()
color("red", "red")
for i in range(2):
    forward(50)
    left(90)

    forward(100)
    left(90)

forward(50)
end_fill()
# 2
begin_fill()
color("blue", "blue")
for i in range(2):
    forward(50)
    left(90)
    forward(100)
    left(90)

forward(50)
end_fill()
# 3+
begin_fill()
color("brown", "brown")
for i in range(2):
    forward(50)
    left(90)
    forward(100)
    left(90)
forward(50)
end_fill()
# 4
begin_fill()
color("yellow", "yellow")
for i in range(2):
    forward(50)
    left(90)
    forward(100)
    left(90)
forward(50)
end_fill()
# 5
begin_fill()
color("gray", "gray")
for i in range(2):
    forward(50)
    left(90)
    forward(100)
    left(90)
forward(50)
end_fill()

print("ok")
mainloop()
# colors = ["red", "blue", "brown", "yellow", "grey"]

























# from turtle import *
#
# shape("arrow")
#
# width(2)
#
# colors = ["red", "blue", "brown", "yellow", "grey"]
#
# for index, line in enumerate(colors):
#     color(line)
#     begin_fill()
#     for i in range(index+1):
#         for i in range(2):
#             right(90)
#             forward(100)
#             right(90)
#             forward(50 * (5 - index))
#     end_fill()
#
# mainloop()
