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
import bisect

# 入力
X = int(input())
Q = int(input())
list_S = [X]

# クエリ
for i in range(Q):
    A, B = map(int, input().split())

    bisect.insort_left(list_S, A)
    bisect.insort_left(list_S, B)

    out = list_S[i + 1]

    # 出力
    print(out)
