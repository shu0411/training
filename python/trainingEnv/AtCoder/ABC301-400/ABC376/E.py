import io
import sys

_INPUT = """\
3
3 2
3 7 6
9 2 4
5 3
6 4 1 5 9
8 6 5 1 7
10 6
61 95 61 57 69 49 46 47 14 43
39 79 48 92 90 76 30 16 30 94
"""
sys.stdin = io.StringIO(_INPUT)

#長さKの部分数列、Aの最大とBの和の積の最小値を求める
#############ここから下をコピペ#############

#入力
T = int(input())

#処理
for _ in range(T):
    N,K = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(N)]
    B = [list(map(int,input().split())) for _ in range(N)]

