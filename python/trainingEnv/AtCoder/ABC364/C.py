import io
import sys

_INPUT = """\
8 30 30
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,X,Y = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

#処理
out = -1
list_A.sort(reverse=True)
list_B.sort(reverse=True)

sum_A = 0
sum_B = 0
for i in range(N):
    sum_A += list_A[i]
    sum_B += list_B[i]
    if sum_A > X or sum_B > Y:
        out = i+1
        break
else:
    out = N

#出力
print(out)