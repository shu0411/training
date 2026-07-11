import io
import sys

_INPUT = """\
2 3
1 2
2 1
1 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())

cnt = 0
dict_row = {i: -1 for i in range(1, N + 1)}
dict_column = {i: -1 for i in range(1, N + 1)}
for _ in range(M):
    R, C = map(int, input().split())
    if dict_row[R] == C:
        cnt -= 1
    else:
        if dict_row[R] != -1:
            cnt -= 1
            dict_column[dict_row[R]] = -1
        if dict_column[C] != -1:
            cnt -= 1
            dict_row[dict_column[C]] = -1
    cnt += 1
    dict_row[R] = C
    dict_column[C] = R

# 出力
print(cnt)
