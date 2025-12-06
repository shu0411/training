import io
import sys

_INPUT = """\
10 5
4 92
1 16
3 77
4 99
2 89
3 8
1 40
5 56
1 40
4 77

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())

# 処理
list_count = [0] * (M + 1)
list_sum = [0] * (M + 1)

for _ in range(N):
    A, B = map(int, input().split())
    list_count[A] += 1
    list_sum[A] += B

for m in range(1, M + 1):
    out = list_sum[m] / list_count[m]

    # 出力
    print(out)
