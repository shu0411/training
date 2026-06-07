import io
import sys

_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())

#処理
out = 0

f_A = 0
list_f_A = [1]
list_f_A_sum_of_digit = [1]
for i in range(1, N+1):
    f_A = sum(list_f_A_sum_of_digit)
    list_f_A.append(f_A)
    f_A_sum_of_digit = sum(list(map(int,list(str(f_A)))))
    list_f_A_sum_of_digit.append(f_A_sum_of_digit)
                
#出力
print(f_A)