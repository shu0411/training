import io
import sys

_INPUT = """\
5 6
    
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
H, W = map(int, input().split())

# 処理
for i in range(H):
    out = ""
    if i == 0 or i == H - 1:
        out = "#" * W
    else:
        out = "#" + "." * (W - 2) + "#"
    # 出力
    print(out)
