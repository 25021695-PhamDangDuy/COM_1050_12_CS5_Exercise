import sys
general = [
    { "start": 0, "end" : 50, "cost" : 1_984}, 
    { "start": 50, "end" : 100, "cost" : 2_050},
    { "start": 100, "end" : 200, "cost" : 2_380},
    { "start": 200, "end" : 300, "cost" : 2_998},
    { "start": 300, "end" : 400, "cost" : 3_350},
    { "start": 400,"end" : float('inf') ,"cost" : 3_460}
]

def calculator_cost_electric(start, end):
    consume_kwh = end - start
    total = 0
    if consume_kwh > 0:
        for i in general:
            if (consume_kwh >= i["start"]):
                distant = min(consume_kwh, i["end"]) - (i["start"] ) 
                total += distant * i["cost"]
            else:
                break
        total *= 1.08 
    elif consume_kwh == 0:
        total = 0
    else:
        print("Số đầu phải nhỏ hơn số cuối!")
        sys.exit()
    return total

user_name_input = input("Nhập tên chủ hộ: ")
try:
    user_input_number_start = float(input("Nhập số điện đầu tháng: "))
    user_input_number_end = float(input("Nhập số điện cuối tháng: "))
except ValueError:
    print("Vui lòng nhập số!")
    sys.exit()

print(f"Họ và tên: {user_name_input} \nSố tiền phải trả là: {calculator_cost_electric(user_input_number_start, user_input_number_end):.0f} VNĐ")


