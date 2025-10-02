#cách 1: sử dụng hàm upper() và lower()
user_input = input("Nhập vào chữ cái: ") #Nhập dữ liệu từ bàn phím
if (len(user_input) != 1):
    print("Chỉ được nhập đúng 1 kí tự")
    exit()
if (ord(user_input) == ord(user_input.upper()) and ord(user_input) == ord(user_input.lower())):#nguyên lí: nếu 1 kí tự đã viết hoa thì mã Unicode của nó sẽ bằng mã Unicode ở dạng in hoa.
    print("Không phải chữ cái")
elif (ord(user_input) == ord(user_input.upper())):
    print(f"Chữ {user_input} là chữ hoa - chữ thường của nó là {user_input.lower()} ")
else:
    print(f"Chữ {user_input} là chữ thường - chữ hoa của nó là {user_input.upper()} ")

#nhược điểm: chỉ xét được trong bảng latin và 1 số ngôn ngữ hệ quả của latin


#cách 2: tính chay
user_input = input("Nhập vào chữ cái: ") #Gán lại giá trị biến user_input
if (len(user_input) != 1):
    print("Chỉ được nhập đúng 1 kí tự")
    exit()
if ( (ord(user_input) >= ord("a"))  and  (ord(user_input) <= ord("z")) ):   #nguyên lí: trong bảng Unicode mã code của a -> z , A -> z, 0 -> 9 là tăng dần 1 đơn vị
    distant = ord(user_input) - ord("a")      #đo xem vị trí của kí tự nhập và so với dãy thực, từ đó suy ra vị trí của kí tự đó so với dãy ánh xạ(in hoa --> thường / in thường -> in hoa)
    upper_user_input = chr( ord("A") + distant )
    print(f"chữ {user_input} là chữ in thường - chữ cái in hoa của nó là {upper_user_input} ")
elif ( (ord(user_input) >= ord("A")) and (ord(user_input) <= ord("Z")) ):
    distant = ord(user_input) - ord("A")
    lower_user_input = chr( ord("a") + distant )
    print(f"chữ {user_input} là chữ in hoa - chữ cái in thường là {lower_user_input}")
else:
    print("Hãy nhập chữ cái latin")
#nhược điểm: các chữ cái ngoài dãy a->z A->Z là lỗi
#Cách 3: Kết hợp 2 cách
user_input = input("Nhập vào chữ cái: ")
unicode_user_input = ord(user_input)
if (len(user_input) != 1):
    print("Chỉ được nhập đúng 1 kí tự")
    exit()
if ((unicode_user_input >= ord("a")) and (unicode_user_input <= ord("z"))):     #kiểm tra giống cách 2 theo nguyên lí - vì cách 2 toàn diện và có thể kiểm tra các kí tụ ngoài vùng làm việc (chữ hán, trung, ..v.v)
    print(f"Đây {user_input} là chữ in thường - chữ in hoa của nó là {user_input.upper()}")  #cách đổi sang bảng ánh xạ giống nguyên lí 1 - vì đơn giản là nó gọn nhưng nhanh thì k biết. vì còn phụ thuộc vào độ phức tạp của hàm upper()
elif ( (unicode_user_input >= ord("A")) and (unicode_user_input <= ord("Z")) ):
    print(f"{user_input} là chữ in hoa - chữ in thường của nó là {user_input.lower()}")
elif ( (unicode_user_input >= ord("0")) and (unicode_user_input <= ord("9"))):
    print(f"{user_input} là số, không phải chữ cái")
else :
    print(f"Đây là kí hiệu không phải chữ cái {user_input}")

#Hướng 4: duyệt list
user_input = (input("Nhập các kí tự, cách nhau bởi dấu cách").split())
for i in user_input:
    unicode_i = ord(i)
    if ((unicode_i >= ord("a")) and (unicode_i <= ord("z"))):
        print(f"{i} là chữ in thường - chữ in hoa của nó là {i.upper()}", end = ",")
    elif ( (unicode_i >= ord("A")) and (unicode_i <= ord("Z")) ):
        print(f"{i} là chữ in hoa - chữ in thường của nó là {i.lower()}")
    elif ( (unicode_i >= ord("0")) and (unicode_i <= ord("9"))):
        print(f"{i} là số, không phải chữ cái")
    else :
        print(f"Đây là kí hiệu không phải chữ cái {i}")

#Hướng 5: dùng hàm islower/isupper
user_input = input("Nhập kí tự: ")
if (len(user_input) != 1):
    print("vui lòng nhập đúng 1 kí tự")
    exit()
if (user_input.islower()):
    print(f"{user_input} là chữ in thường - chữ in hoa là {user_input.upper()}")
elif (user_input.isupper()):
    print(f"{user_input} là chữ in hoa - chữ in thường là {user_input.lower()}")
elif (user_input.isdigit()):
    print(f"{user_input} là chữ số")
else:
    print("không phải chữ cái")
#Vấn đề tiếp : nhập quá 2 kí tự thì program sẽ lỗi + và còn chữ cái của tiếng việt ư ắ