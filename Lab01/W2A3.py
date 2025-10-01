#Nhập dữ liệu
a = int(input("Nhập dữ liệu của a: "))
b = int(input("Nhập dữ liệu của b: "))
#Tính toán
sum = a + b
sub = a - b
muti = a * b
div = a / b
modul = a % b 
floorDiv = a // b
#Hiển thị kết quả
print("== Kết quả phép tính ==")
print(f"{a} + {b} = {sum}")
print(f"{a} - {b} = {sub}")
print(f"{a} x {b} = {muti}")
print(f"{a} / {b} = {div}")
print(f"{a} % {b} = {modul}")
print(f"{a} // {b} = {floorDiv:.2f}")

