import io
import sys

_INPUT = """\
37 39 93
Blue
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
list_RGB = list(map(int, input().split()))
S = input()

#処理
out = 0
if S == "Red":
    out = min(list_RGB[1], list_RGB[2])
elif S == "Green":
    out = min(list_RGB[0], list_RGB[2])
else:
    out = min(list_RGB[0], list_RGB[1])

#出力
print(out)