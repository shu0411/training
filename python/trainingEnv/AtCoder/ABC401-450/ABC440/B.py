import io
import sys

_INPUT = """\
8
72 74 69 70 73 75 71 77

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_T = list(map(int, input().split()))

# 処理
list_idx_T = []
for i, T in enumerate(list_T):
    list_idx_T.append((i + 1, T))

list_idx_T.sort(key=lambda x: x[1])

list_out = []
for idx, _ in list_idx_T[:3]:
    list_out.append(idx)

# 出力
print(*list_out)
