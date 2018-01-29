<<<<<<< HEAD
# Exercise 1
# Given the following dictionary:
# inventory = {
#     'gold' : 500,
#     'pouch' : ['flint', 'twine', 'gemstone'],
#     'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
# }
# Try to do the followings:
# Add a key to inventory called 'pocket'.
# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
# Then .remove('dagger') from the list of items stored under the 'backpack' key.
# Add 50 to the number stored under the 'gold' key.
#####################################################
# Bài tập 1
# Cho từ điển sau:
# inventory = {
#      'vàng': 500,
#      'túi': ['đá lửa', 'sợi xoắn', 'đá quý'],
#      'ba lô': ['xylophone', 'dao găm', 'giường ngủ', 'ổ bánh mì']
# }
# Cố gắng làm như sau:
# Thêm chìa khóa vào khoảng không quảng cáo được gọi là 'túi'.
# Đặt giá trị của 'túi' là một danh sách bao gồm chuỗi 'seashell', 'lạ berry', và 'lint'.
# Sau đó, gỡ bỏ ('dao găm') từ danh sách các đồ vật được lưu trữ dưới phím 'ba lô'.
# Thêm 50 vào số được lưu trữ dưới phím 'vàng'.
# Anh Huy giúp

inventory = {
    'gold' : 500, # kieu integer rồi
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# 1 thêm pocket có list các phần tử trong nó vào enventory
inventory ['pocket'] = ['seashell', 'strange berry','lint']
print(inventory)
# 2 xóa một phần tử ('dagger') trong list ['backpack']
inventory ['backpack'].remove('dagger')
print(inventory)
# 3 Ở key 'gold' tăng giá trị thêm 50 số vào

inventory['gold'] += 50
print(inventory['gold'])
=======
# Exercise 1
# Given the following dictionary:
# inventory = {
#     'gold' : 500,
#     'pouch' : ['flint', 'twine', 'gemstone'],
#     'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
# }
# Try to do the followings:
# Add a key to inventory called 'pocket'.
# Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
# Then .remove('dagger') from the list of items stored under the 'backpack' key.
# Add 50 to the number stored under the 'gold' key.
#####################################################
# Bài tập 1
# Cho từ điển sau:
# inventory = {
#      'vàng': 500,
#      'túi': ['đá lửa', 'sợi xoắn', 'đá quý'],
#      'ba lô': ['xylophone', 'dao găm', 'giường ngủ', 'ổ bánh mì']
# }
# Cố gắng làm như sau:
# Thêm chìa khóa vào khoảng không quảng cáo được gọi là 'túi'.
# Đặt giá trị của 'túi' là một danh sách bao gồm chuỗi 'seashell', 'lạ berry', và 'lint'.
# Sau đó, gỡ bỏ ('dao găm') từ danh sách các đồ vật được lưu trữ dưới phím 'ba lô'.
# Thêm 50 vào số được lưu trữ dưới phím 'vàng'.


inventory = {
    'gold' : 500, # kieu integer rồi
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# 1 thêm pocket có list các phần tử trong nó vào enventory
inventory ['pocket'] = ['seashell', 'strange berry','lint']
print(inventory)
# 2 xóa một phần tử ('dagger') trong list ['backpack']
inventory ['backpack'].remove('dagger')
print(inventory)
# 3 Ở key 'gold' tăng giá trị thêm 50 số vào

inventory['gold'] += 50
print(inventory['gold'])

# Em đã hiểu về thêm xửa xóa dữ liệu rồi ạ, cẩn thận về dấu và cú pháp
>>>>>>> 8abc8e53cfabba275c0bbc2837ca1fec99c452f2
