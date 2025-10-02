user_input = input("Nhập kí tự cần kiểm tra: ")
if len(user_input) != 1:
    print("Vui lòng nhập 1 kí tự")
    exit()
if (user_input.isdigit()):
    print(f"{user_input} là số")
elif (user_input.isalpha()):
    print(f"{user_input} là chữ cái")
else:
    print("là kí tự")