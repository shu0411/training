import io
import sys

_INPUT = """\
3
40 40 100
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int,input().split()))

#処理
out = 0
while True:
    list_A.sort(reverse=True)

    if list_A[1] <= 0:
        break

    list_A[0] -= 1
    list_A[1] -= 1
    out += 1

#出力
print(out)