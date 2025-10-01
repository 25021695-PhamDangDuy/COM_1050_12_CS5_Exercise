import math
user_input = input("Nhập vào 2 số đo kích thước mảnh vườn: ").split()
don_vi = input("Nhập đơn vị kích thước: ")
if len(user_input) != 2:
    print("vui lòng nhập đủ 2 kích thước")
    exit()
a , b = map(float, user_input)
chieu_dai = max(a , b)
chieu_rong = min(a , b)
ban_kinh = chieu_rong / 2
s_square = chieu_dai * chieu_rong
s_circle = 3.14 * (ban_kinh ** 2)
s_answer = s_square - s_circle
print(f"Phần diện tích còn lại là: {s_answer:.2f} {don_vi}")