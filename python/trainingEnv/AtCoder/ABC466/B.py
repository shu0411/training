import io
import sys

_INPUT = """\
5 5
2 6
5 12
5 2
5 9
2 7

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
dict_max = {i: -1 for i in range(1, M + 1)}
for _ in range(N):
    C, S = map(int, input().split())
    dict_max[C] = max(dict_max[C], S)

# 出力
out = list(dict_max.values())
print(*out)
