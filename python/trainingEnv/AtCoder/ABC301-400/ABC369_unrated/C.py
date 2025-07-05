import io
import sys

_INPUT = """\
4
3 6 9 3
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))

#処理
out = N #長さ1の等差数列
list_diff = []
for i in range(N-1):
    list_diff.append(list_A[i+1] - list_A[i])

tmp = 1 #同じ差が続いている数
for i in range(N-2):
    if list_diff[i] == list_diff[i+1]:
        tmp += 1
    else:
        tmp = 1
    out += tmp

if N >= 2:
    out += 1    #最後の2つの分

#出力
print(out)