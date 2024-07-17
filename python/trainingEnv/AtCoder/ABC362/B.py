import io
import sys

_INPUT = """\
2 4
-3 2
1 -2
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

#処理
#２点間の距離の2乗
def distance(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

AB = distance(A[0], A[1], B[0], B[1])
BC = distance(B[0], B[1], C[0], C[1])
AC = distance(A[0], A[1], C[0], C[1])

out = "No"

#三角形ABCが直角三角形かどうか
if AB + BC == AC or BC + AC == AB or AC + AB == BC:
    out = "Yes"

#出力
print(out)