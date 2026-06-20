import io
import sys

_INPUT = """\
108 192

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
X,Y = map(int,input().split())

# 処理
if X / 16 == Y / 9:
    out = "Yes"
else:
    out = "No"

# 出力
print(out)
