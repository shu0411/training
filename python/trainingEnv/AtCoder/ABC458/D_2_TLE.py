import io
import sys

_INPUT = """\
278117031
7
167642909 517897721
148434323 567739597
319926999 481642530
659199879 252516557
49913403 798318034
89701408 892537201
199166668 742285869

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import numpy

# 入力
X = int(input())
Q = int(input())
list_S = [X]

# クエリ
for i in range(Q):
    A, B = map(int, input().split())

    list_S.append(A)
    list_S.append(B)

    out = int(numpy.quantile(list_S, 0.5))

    # 出力
    print(out)
