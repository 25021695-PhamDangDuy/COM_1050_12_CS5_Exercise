try:
    user_input = int(input("Nhập vào số nguyên cần kiểm tra: "))
    last_digit = user_input % 10
    print((last_digit == 5))
except ValueError:
    print("Chỉ được nhập số nguyên!")