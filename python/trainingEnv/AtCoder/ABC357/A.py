import io
import sys

_INPUT = """\
5 10
2 3 2 3 5
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int,input().split())
list_H = list(map(int,input().split()))

#処理
sum_H = 0
for i,h in enumerate(list_H):
    sum_H += h
    if sum_H > M:
        print(i)
        break
else:
    print(N)