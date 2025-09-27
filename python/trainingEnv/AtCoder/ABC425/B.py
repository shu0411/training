import io
import sys

_INPUT = """\
7
3 -1 4 -1 5 -1 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))

#処理

minus_count = 0
dic_A = {i: 0 for i in range(1, N + 1)}

for a in list_A:
    if a == -1:
        minus_count += 1
    elif 1 <= a <= N:
        dic_A[a] += 1

list_zero = [k for k, v in dic_A.items() if v == 0]
zero_count = len(list_zero)

# 出力
if zero_count <= minus_count:
    print("Yes")
    list_out = []
    for a in list_A:
        if a == -1:
            list_out.append(list_zero.pop())
        else:
            list_out.append(a)
    print(*list_out)

else:
    print("No")
