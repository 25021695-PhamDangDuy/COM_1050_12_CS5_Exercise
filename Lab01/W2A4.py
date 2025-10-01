a1, b1, c1, a2, b2, a3 = map(float, input("Nhập lần lượt dữ liệu a1, b1, c1, a2, b2, a3: ").split())
average = ((a1 + b1 + c1) + (a2 + b2)*2 + a3*3)/10
print(f"Điểm trung bình là: {average:.1f}")
