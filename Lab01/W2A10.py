#Nhập vào 3 người
nameInput = input("Nhập vào lần lượt ba tên người: ").split()

if len(nameInput) != 3:
    print("Lỗi số người đã nhập! Vui lòng nhập đúng 3 tên người!")
else:
    nameInput.reverse() 
    print(f"Xin chào bạn {nameInput[0]}, {nameInput[1]} và {nameInput[2]}")
