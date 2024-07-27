import io
import sys

_INPUT = """\
6
salty
sweet
salty
salty
sweet
sweet
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())

#処理
before_S = ""
out = "Yes"
for i in range(N-1):    #最後は気持ち悪くなっても食べられる。
    S = input()
    if before_S == "sweet" and S == "sweet":
        out = "No"
        break
    before_S = S

print(out)