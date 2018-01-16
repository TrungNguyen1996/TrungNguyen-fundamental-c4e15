#   Viết một chương trình yêu cầu người sử dụng chiều cao (cm) và trọng lượng (kg), và sau đó tính BMI (Body Mass Index):
# BMI = khối lượng (kg) / (chiều cao (m) x chiều cao (m))
#   Lưu ý: bạn phải thực hiện chuyển đổi từ cm đến m trước khi tính
# Sau đó, dựa trên BMI, nói với họ rằng họ là:
  # Thiếu cân  nghiêm trọng nếu BMI <16
  # Thiếu cân nhẹ nếu BMI nằm trong khoảng từ 16 đến 18,5
  # Bình thường nếu BMI nằm trong khoảng từ 18,5 đến 25
  # Thừa cân nếu BMI giữa 25 và 30
  # Béo phì nếu BMI lớn hơn 30
    # Triển khai
#  Bước 1: Khai báo đôi tượng sử dụng là biến số x y ... nhập vàp vs đinh dạng int, vs in ra câu hỏi Có gán đơn vị đo
#  Bước 2: Để tính chỉ số BIM thì đặt BIM là (=) giá trịcủa công thức nhân của
#  Bước 3 rồi tạo vòng for cho nó so sánh (map: hình thoi). ra điểu kiệm cho 3 phần
    # ĐK 1: Thiếu cân  nghiêm trọng nếu BMI <16
    # ĐK 2: Thiếu cân nhẹ nếu BMI nằm trong khoảng từ 16 đến (dưới) 18,5
    # ĐK 3: Bình thường nếu BMI nằm trong khoảng từ 18,5 đến (dưới) 25
    # ĐK 3: Thừa cân nếu BMI giữa 25 và 30
    # ĐK 3: Béo phì nếu BMI lớn hơn 30

x = int (input("Nhập vào chiều cao: "))
cao = x / 100
print (cao, "meter")
y = int (input("Nhập vào cân nặng: "))
print (y,"kg")
BMI =  y / x**2
#  BMI =  y / x*x
#  so sánh về điều kiến cho tất cả từ các dòng cùng cấp, làm gì của dòng nào thì nó thẳng hàng
if BMI < 16:
    print ("Thiếu cân trầm trọng - Severely")
#
elif BMI < 18.5:
    print ("Thiếu cân nhẹ - Underweight")
#
elif BMI < 25:
    print("Bình thường - Normal")
#
elif BMI < 30:
    print ("Thừa cân - Overweight")
#
else:
    print ("Béo phì - Obese")

print ("Cảm ơn bạn đã đến khám")

#  Sau if cú pháp phải có : hai chấm
#  Vòng lặp sau cũng có : hai chấm
