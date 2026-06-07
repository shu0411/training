import io
import sys

_INPUT = """\
6 9
3 6
2 5
2 3
4 3
1 5
6 2
3 1
5 3
2 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
dic_rel = {i: 0 for i in range(1, N + 1)}
for _ in range(M):
    A, B = map(int, input().split())
    dic_rel[A] += 1
    dic_rel[B] += 1

# 処理
out = [0] * (N + 1)
for i in range(1, N + 1):
    cnt = N - dic_rel[i] - 1
    if cnt >= 3:
        out[i] = cnt * (cnt - 1) * (cnt - 2) // 6

# 出力
print(*out[1:])
