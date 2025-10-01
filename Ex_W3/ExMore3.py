try:
    user_input = int(input("Nhập số nguyên cần kiểm tra: "))
    print((user_input % 3 == 0) and (user_input % 5 == 0))
except ValueError:
    print("chỉ được nhập số nguyên")