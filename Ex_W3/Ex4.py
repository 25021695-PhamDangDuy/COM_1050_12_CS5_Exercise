#Cách 1: tính chay
user_input = input("Nhập vào kí tự cần kiểm tra: ")
if (len(user_input) != 1):
    print("vui lòng nhập đúng 1 kí tự")
    exit()
if (  (user_input != user_input.upper()) or (user_input != user_input.lower()) ):   #Nguyên lí: nếu kí tự nhập vào là 1 chữ cái thì sẽ có dạng in hoa - in thường và ngược lại nếu đó là số / kí hiệu thì chỉ có 1 dạng duy nhất
    print(f"{user_input} là chữ cái alphabet")
else:
    print(f"{user_input} không phải chữ cái alphabet")

#Cách 2: dùng hàm isalpha()
user_input = input("Nhập vào kí tự cần kiểm tra: ")
if (len(user_input) != 1):
    print("Không phải 1 kí tự")
    exit()
if user_input.isalpha():
    print(f"{user_input} là chữ cái alphabet")
else: 
    print("Không phải chữ cái alphabet")

