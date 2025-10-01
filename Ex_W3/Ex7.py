user_input = input("Nhập chuỗi bạn muốn: ")
if (len(user_input) >= 20):
    print(f"kí tự thứ 5 là {user_input[4]}, kí tự thứ 9 là {user_input[8]}")
else:
    print("chưa đủ 20 kí tự trở lên")