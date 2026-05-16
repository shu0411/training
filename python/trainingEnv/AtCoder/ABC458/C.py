import io
import sys

_INPUT = """\
SMBCPROGRAMMINGCONTEST

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
list_c_idx = []
for i, s in enumerate(list(S)):
    if s == "C":
        list_c_idx.append(i)

out = 0
len_S = len(S)
for c_idx in list_c_idx:
    out += min(c_idx + 1, len_S - c_idx)

# 出力
print(out)
