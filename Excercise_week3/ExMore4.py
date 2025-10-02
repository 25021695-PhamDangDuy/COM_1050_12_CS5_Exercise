try:
    user_birthyear = int(input("Nhập năm sinh: "))
    years_now = int(input("Nhập năm hiện tại: "))
    age = years_now - user_birthyear
    if (age >= 18):
        print(f"đủ đi bầu cử")
    else:
        print(f"chưa đủ")
except ValueError:
    print("Chỉ được nhập năm!")