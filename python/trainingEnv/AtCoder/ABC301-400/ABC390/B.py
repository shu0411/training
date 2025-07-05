import io
import sys

_INPUT = """\
3
36 12 4
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))

#処理
out = "Yes"
before_A = -1
times = 0
for i,A in enumerate(list_A):
    if i == 1:
        times = A / before_A
    elif i > 1:
        if A != before_A * times:
            out = "No"
    before_A = A
    if out == "No":
        break

#出力
print(out)