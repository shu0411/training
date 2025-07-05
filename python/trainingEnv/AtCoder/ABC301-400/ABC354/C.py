import io
import sys

_INPUT = """\
6
32 101
65 78
2 29
46 55
103 130
52 40
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_iAC = []
for i in range(1,N+1):
    a, b = map(int, input().split())
    list_iAC.append([i, a, b])

#処理
list_iAC.sort(key=lambda x: x[1])
new_list_i = []
before_C = 0
for iAC in list_iAC[::-1]:
    if len(new_list_i) == 0:
        new_list_i.append(iAC[0])
        before_C = iAC[2]
    if before_C > iAC[2]:
        new_list_i.append(iAC[0])
        before_C = iAC[2]

#出力
print(len(new_list_i))
print(" ".join(map(str, sorted(new_list_i))))