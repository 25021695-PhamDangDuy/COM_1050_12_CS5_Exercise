ranking = [
    {"ranked" : "Giỏi" , "start": 8, "end" : 10},
    {"ranked" : "Khá" , "start": 6.5, "end" : 8},
    {"ranked" : "Trung Bình" , "start": 5, "end" : 6.5},
    {"ranked" : "Yếu" , "start": 0, "end" : 5}
]

def checking_ranking(score):
    if (score < 0 or score > 10):
        print("điểm trong khoảng 0 - 10")
        exit()
    if (score == 10):
        print("Học lực loại giỏi")
    for i in ranking:
        if ( score >= i["start"] and score < i["end"]):
            ranked = i["ranked"]
            print(f"Học lực loại {ranked}")
        
    return

try:
    user_score = float(input("Nhập điểm của bạn: "))
    checking_ranking(user_score)
except ValueError:
    print("chỉ được nhập số")


    