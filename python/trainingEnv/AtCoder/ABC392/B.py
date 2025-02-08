import io
import sys

_INPUT = """\
9 1
9
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int, input().split())
list_A = list(map(int, input().split()))

#処理
out_list = []
for i in range(1, N+1):
    if i not in list_A:
        out_list.append(i)

#出力
print(len(out_list))
print(*out_list)