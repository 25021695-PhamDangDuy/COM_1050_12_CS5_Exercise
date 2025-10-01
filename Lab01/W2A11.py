hour = float(input("Nhập số giờ: "))
minute = float(input("Nhập số phút: "))
#Đổi
hourToSecond = hour * 3600
minuteToSecond = minute * 60
totalSecond = hourToSecond + minuteToSecond
#In
print(f"Quy đổi: \n -{hour} giờ = {hourToSecond} giây \n -{minute} phút = {minuteToSecond} giây \n Tổng = {totalSecond} giây")