try:
    user_input = int(input("Nhập vào số nguyên cần kiểm tra: "))
    if (user_input % 2 == 0) :
        print(f"{user_input} là số chẵn")
    else:
        print(f"{user_input} là số lẻ")
except ValueError:
    print("chỉ được nhập số nguyên")