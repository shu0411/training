import io
import sys

_INPUT = """\
54231
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
input_X = input()

# 処理
list_X = sorted(list(input_X))
for i, x in enumerate(list_X):
    if x == "0":
        continue
    else:
        out = list_X.pop(i)
        break

for x in list_X:
    out += x

# 出力
print(out)
