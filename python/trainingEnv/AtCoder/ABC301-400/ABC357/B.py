import io
import sys

_INPUT = """\
SunTORYaa
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
count_lower = 0
count_upper = 0
for s in S:
    if s.islower():
        count_lower += 1
    else:
        count_upper += 1

if count_upper > count_lower:
    out = S.upper()
else:
    out = S.lower()

#出力
print(out)