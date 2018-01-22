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
# R
shop = ["T-Shirt","Sweater"]
ans = input("Welcome to our shop, what do you want") # nhap hang rui cho chon
if ans == "r":  # neu an thi lam: in [] la cua cai list
    print(shop)
elif ans == "c":
    new_item = input("Please enter your new item ???:  ")
    shop.append(new_item)
    print(shop)

elif ans == "d":
