import io
import sys

_INPUT = """\
10
68 3
17 2
99 2
92 4
82 4
10 3
100 2
78 1
3 1
35 4
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())

#処理
dict_C = {}
for i in range(N):
    A, C = map(int, input().split())
    if C in dict_C:
        dict_C[C] = min(dict_C[C], A)
    else:
        dict_C[C] = A

#dict_Cの中の最大の値を取り出す
min_A = max(dict_C.values())
print(min_A)
