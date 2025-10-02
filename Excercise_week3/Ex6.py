#Ý tưởng: chứng minh với 3 số a, b, c nếu tìm được số lớn nhất trong 3 số thì có thể xét tam giác đơn giản
#Chứng minh: cho 3 số dương a, b, c bất kì. nếu max(a,b,c) < sum(2 số còn lại) thì đó là tam giác
#Giải thích: TH1: a != b != c => giả sử c là max() thì c > a, b. Và đồng thời giả sử điều kiện max < sum là đúng thì c < a + b. Từ đó các bđt sau luôn đúng c + a > b và c + b > a
#            TH2: a = b = c => ta có đẳng thức 2x > x với x = a, b, c luôn đúng do đó nó là 1 tam giác
#            TH3: 2/3 số đo bằng nhau
#                Th3.1: a = b và max = c => nếu max < sum thì c > 2a  do đó. c + a > a hay c + a > b tương tự với c + b
#                Th3.2: b = c và max = c = b => nếu vậy chắc chắn sum > max vì (x + a > x) do đó luôn là 1 tam giác
# -> hết trường hợp tồn tại
#====> Tóm lại chỉ cần thỏa mãn điều kiện cần max < sum thì sẽ thỏa mãn điều kiện còn lại -> là tam giác
import sys
number_input = (input("Nhập vào 3 số dương bất kì để kiểm tra: ").split())

def check_list(list_need_to_check):
    if len(list_need_to_check) != 3:
        print("vui lòng nhập đúng 3 số đo")
        sys.exit()
    for i in list_need_to_check:
        try:
            float(i)
        except ValueError:
            print(f"{i} không phải là số")
            sys.exit()

        if (float(i) <= float(0)):
            print(f"{i} không phải số dương")
            sys.exit()


def check_triangle(first, second, third):
    max_size = max(first, second, third)
    sum_two_size_except_max = (first + second + third) - max_size
    if (sum_two_size_except_max >= max_size):
        print("Là tam giác")
    else:
        print("Không là tam giác")

check_list(number_input)
a, b, c = map(float, number_input)
check_triangle(a, b, c)

