try:
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    if (a == b):
        print("Bằng nhau")
    else:
        print(f"số lớn nhất là {max(a,b)}")
except ValueError:
    print("Chỉ được nhập số")