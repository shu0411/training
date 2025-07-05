import io
import sys

_INPUT = """\
|-|-|-|------|
"""
sys.stdin = io.StringIO(_INPUT)
#out : 3 1 4 1 5
#############ここから下をコピペ#############

#入力
S = input()

#処理
out_list = []
tmp_out = 0
first = True
for s in S:
    if first:
        first = False
        continue
    if s == "|":
        out_list.append(tmp_out)
        tmp_out = 0
    else:
        tmp_out += 1

#出力
print(*out_list)