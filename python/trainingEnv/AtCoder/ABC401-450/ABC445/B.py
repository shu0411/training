import io
import sys

_INPUT = """\
6
abc
d
efghi
jkl
mnopq
r

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())

list_S = []
max_len = 0
for _ in range(N):
    S = input()
    max_len = max(len(S), max_len)
    list_S.append(S)

# 処理
for s in list_S:
    len_s = len(s)
    dot_count = (max_len - len_s) // 2
    out = "." * dot_count + s + "." * dot_count

    # 出力
    print(out)
