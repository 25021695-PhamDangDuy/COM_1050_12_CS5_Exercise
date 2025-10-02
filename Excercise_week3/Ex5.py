import sys
user_input = input("Nhập vào chữ cái: ")
def check_length(char):
    if len(char) != 1:
        print("vui lòng nhập đúng 1 kí tự")
        sys.exit()
check_length(user_input)

def change_char(input_function):
    print(f"Chữ liền trước 1 đơn vị là {chr(ord(input_function) - 1).lower()}")

if user_input.isalpha():
    if user_input.islower():
        print("Đây là chữ in thường")
    elif user_input == "A":
        print("không có chữ liền trước")
    else:
        change_char(user_input)
elif user_input.isdigit():
    print("Là chữ số!")
else:
    print(f"{user_input} không phải chữ cái")