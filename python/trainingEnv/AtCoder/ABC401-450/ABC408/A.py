import io
import sys

_INPUT = """\
10 22
47 81 82 95 117 146 165 209 212 215
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,S = map(int, input().split())
list_T = list(map(int, input().split()))

#処理
out = "Yes"
before_T = 0
diff = 0
for T in list_T:
    diff = T - before_T
    before_T = T
    if diff > S + 0.5:
        out = "No"
        break

#出力
print(out)