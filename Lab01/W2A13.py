a , b = map(int,input("Nhập giá trị của a và b: ").split())
Caculator = (a * b) % 10
print(f" Chữ số hàng đơn vị của phép tính: {a} x {b} là: {Caculator}")
print(f"Explain: \n - đặt a * b = c \n - thì c sẽ là một số có dạng a1a2a3...an = (a1a2...a(n-1)*10 + an) \n - khi đó / 10 lấy dư sẽ ra an")
