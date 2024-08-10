import io
import sys

_INPUT = """\
8
1 2
1 2
3
2 2
1 4
1 4
2 2
3
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
Q = int(input())

#処理
group = {}
for i in range(Q):
    inputs = input().split()
    n = int(inputs[0])
    x = int(inputs[1]) if len(inputs) > 1 else None

    if n == 1:
        if x in group:
            group[x] += 1
        else:
            group[x] = 1
    elif n == 2:
        group[x] -= 1
        if group[x] == 0:
            del group[x]
    else:
        print(len(group))
