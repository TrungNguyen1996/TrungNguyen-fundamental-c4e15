<<<<<<< HEAD
# Hoàn thành bài tập CRUD trong lớp học, mô phỏng một cửa hàng quần áo
# Chào mừng đến cửa hàng của chúng tôi, bạn muốn gì (C, R, U, D)? R
#     Các mặt hàng của chúng tôi: áo thun, áo len
# Chào mừng đến cửa hàng của chúng tôi, bạn muốn gì (C, R, U, D)? C
#     Nhập mục mới: Jeans
# Các mặt hàng của chúng tôi: T-Shirt, Sweater, Jeans
# Chào mừng đến cửa hàng của chúng tôi, bạn muốn gì (C, R, U, D)? Bạn
# Cập nhật vị trí? 2
#     Vật phẩm mới? Váy
# Các mặt hàng của chúng tôi: T-Shirt, Váy, Jeans
# Chào mừng đến cửa hàng của chúng tôi, bạn muốn gì (C, R, U, D)? D
#     Xóa vị trí? 3
# Các mặt hàng của chúng tôi: áo thun, váy
# Xử lý các trường hợp ngoại lệ (trên, thấp hơn trường hợp, chỉ số ra khỏi phạm vi) cho mình

# 2.1
shop = ["T-Shirt","Sweater"]
answer = input("Chào mừng bạn đến với cửa hàng, bạn cần gì nhỉ") # nhap hang rui cho chon
if answer == "r":  # neu an thi lam: in [] la cua cai list
    print(shop)
elif answer == "c":
    new_item = input("Mời bạn nhập vào sản phẩm ???:  ")
    shop.append(new_item)
    print(shop)
elif answer == "u":
    position = int(input("Bạn muốn update vào vị trí nào"))
    new_value = input("Mời bạn nhập vào mới")
    shop[position -1] = new_value
    print(shop)
elif answer == "d":
    position = int(input("Bạn muốn xóa vị trí nào"))

    shop.pop (position -1)
    print(shop)

# elif resp.lower() == "u":
#         update = int(input("Update position? "))
#         new_item = input("New item? ")
#         if update <= len(shop):
#             shop[update -1] = new_item
#             print("Our items:" *shop, sep=", ")
#         else:
#             print("Item slot is empty")
































# clothes = ["T-Shirt", "Sweater"]
# choice = ["C", "R", "U", "D"]
# Loop = True
# while Loop:
#     CRUD = input("Welcome to our shop, what do you want {0}? ".format(choice))
#     if CRUD == "C":
#         new = input("Enter new item: ")
#         clothes.append(new)
#     elif CRUD == "R":
#         pass
#     elif CRUD == "U":
#         new_po = int(input("Update position? "))
#         new = input("New item? ")
#         clothes[new_po - 1] = new
#     elif CRUD == "D":
#         del_po = int(input("Delete position? "))
#         clothes.pop(del_po - 1)
#     else:
#         print("please only choose in {0}".format(choice))
#         break
#     print("Our items:", end =" ")
#     print(*clothes, sep =", ")
# # else:
# #     print()
=======
# Hoàn thành bài tập CRUD trong lớp học, mô phỏng một cửa hàng quần áo
# Chào mừng đến cửa hàng của chúng tôi, bạn muốn gì (C, R, U, D)? R
#     Các mặt hàng của chúng tôi: áo thun, áo len
# Chào mừng đến cửa hàng của chúng tôi, bạn muốn gì (C, R, U, D)? C
#     Nhập mục mới: Jeans
# Các mặt hàng của chúng tôi: T-Shirt, Sweater, Jeans
# Chào mừng đến cửa hàng của chúng tôi, bạn muốn gì (C, R, U, D)? Bạn
# Cập nhật vị trí? 2
#     Vật phẩm mới? Váy
# Các mặt hàng của chúng tôi: T-Shirt, Váy, Jeans
# Chào mừng đến cửa hàng của chúng tôi, bạn muốn gì (C, R, U, D)? D
#     Xóa vị trí? 3
# Các mặt hàng của chúng tôi: áo thun, váy
# Xử lý các trường hợp ngoại lệ (trên, thấp hơn trường hợp, chỉ số ra khỏi phạm vi) cho mình

# 2.1
shop = ["T-Shirt","Sweater"]
answer = input("Chào mừng bạn đến với cửa hàng, bạn cần gì nhỉ") # nhap hang rui cho chon
if answer == "r":  # neu an thi lam: in [] la cua cai list
    print(shop)
elif answer == "c":
    new_item = input("Mời bạn nhập vào sản phẩm ???:  ")
    shop.append(new_item)
    print(shop)
elif answer == "u":
    position = int(input("Bạn muốn update vào vị trí nào"))
    new_value = input(shop)
    new_value = shop[update -1]
    print(shop)
elif answer == "d":
    position = int(input("Bạn muốn xóa vị trí nào"))

    shop.pop (position -1)
    print(shop)
    
    Khổ ghê a huhu.
>>>>>>> 8abc8e53cfabba275c0bbc2837ca1fec99c452f2
