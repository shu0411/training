import io
import sys

_INPUT = """\
WWWWWWW

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
count_E = 0
count_W = 0
for s in S:
    if s == "E":
        count_E += 1
    else:
        count_W += 1

if count_E > count_W:
    out = "East"
else:
    out = "West"

# 出力
print(out)
