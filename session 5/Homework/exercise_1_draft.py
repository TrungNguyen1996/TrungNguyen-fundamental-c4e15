nguyen = {
    'name': 'nguyen dep trai',
    'age': 22,
    'home': 'hanoi',
    'height' : 160,
    'weight' : 60,      # kiểu int ko có nháy kép
    'hair color' : 'black',
    'bag' : ['lenovo', 'mouse', 'keyboat', 'pen']
}
# 1 in ra tất cả
# # print(nguyen, ['name'])
# print( nguyen['name'])
# print( nguyen['age'])
# print( nguyen['home'])
# print( nguyen['height'])
# print( nguyen['weight']) # len 62 kg
# print( nguyen['hair color'])

# 2 in ra từng cái một bởi key
# nguyen ['weight'] += 2 # = 62 /  nó bằng nó + với 2 len 2kg
# print(nguyen['weight'])
# print(nguyen["bag"])
# in ra từng cá
for key, value in nguyen.items():
    print(key, value)
