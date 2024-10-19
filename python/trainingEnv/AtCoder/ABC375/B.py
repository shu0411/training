import io
import sys

_INPUT = """\
5
-100000 100000
100000 -100000
-100000 100000
100000 -100000
-100000 100000
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

import math
#入力
N = int(input())

#処理
before_X = 0
before_Y = 0
cost = 0
for _ in range(N):
    X,Y = map(int, input().split())
    cost += math.sqrt((X-before_X)**2 + (Y-before_Y)**2)
    before_X = X
    before_Y = Y

#最後の点から(0,0)までの距離を足す
cost += math.sqrt((0-before_X)**2 + (0-before_Y)**2)

#出力
print(cost)