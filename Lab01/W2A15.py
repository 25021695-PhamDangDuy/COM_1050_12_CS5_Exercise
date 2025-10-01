n =int(input("Nhập số n nguyên dương: "))
if n <= 0:
    print("Hãy nhập số nguyên dương!")
else:
    star_number = 6*n*(n - 1) + 1
    print(f"Số sao là: {star_number}")
#Giải thích công thức:
#Với n = 1 -> addition = 1 + 6 + 6x(-1)
#Với n = 2 -> addition = 6 + 6x1
#với n = 3 -> addition = 6 + 6x3
#với n = 4 -> addition = 6 + 6x5
#.......
#với  n = k -> addition = 6 + 6x(2k-3) = 6x(2k-2) = 12x(k-1) (k>=1)
#Total(tổng) = số sao cần tìm = star_number = n1 + n2 + n3 + .... n(k) = 1 + 12x(0 + 2 + 4 + ... + k-1) = 1 + 12x( (((k-1) +1 ) x k)/2 )= 1 + 6k(k-1)