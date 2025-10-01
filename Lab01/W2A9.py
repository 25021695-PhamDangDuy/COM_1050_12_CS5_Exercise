price = float(input("Chiếc đồng hồ giá (USD): "))
#Thuế Nhập khẩu
FOB = price*(30/100)
#Thuế VAT
VAT = price*(10/100)
#Chi phí vận chuyển
Ship = 10
#Tính
CostOff = price + VAT + FOB + Ship
#In kết quả
print(f"Chi phí phải bỏ ra gồm: \n -Thuế nhập khẩu: {FOB} USD \n -Phí VAT: {VAT} USD \n -Phí vận chuyển: {Ship} USD \n => Tổng = {CostOff} USD")