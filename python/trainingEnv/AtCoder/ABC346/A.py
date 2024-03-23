import io
import sys

_INPUT = """\
5
22 75 26 45 72
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))

#処理
out = ""
tmp_before_A = list_A[0]

for i in range(1, N):
    by_A = tmp_before_A * list_A[i]
    out += str(by_A) + " "
    tmp_before_A = list_A[i]

#出力
print(out[:-1]) #最後のスペースを削除