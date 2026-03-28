import io
import sys

_INPUT = """\
10 5
3 2
3 4
1 2
2 2
4 4
3 1
3 4
4 2
3 3
3 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())

dict_now = {i: 0 for i in range(1, M + 1)}
dict_next = {i: 0 for i in range(1, M + 1)}

for i in range(N):
    A, B = map(int, input().split())
    dict_now[A] += 1
    dict_next[B] += 1

# 処理
for i in range(1, M + 1):
    out = dict_next[i] - dict_now[i]
    # 出力
    print(out)
