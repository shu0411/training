import io
import sys

_INPUT = """\
8 3
31 43 26 6 18 36 22 13
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N, K = map(int, input().split())
list_A = list(map(int, input().split()))

#処理
list_A.sort()
min_diff = 10**9
for i in range(K+1):
    diff = list_A[i+N-K-1] - list_A[i]
    if diff < min_diff:
        min_diff = diff

#出力
print(min_diff)