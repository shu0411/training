import io
import sys

_INPUT = """\
-512
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import math
#入力
N = input()

#処理
if len(N) <= 2:
    out = math.ceil(int(N) / 10)
else:
    intN10 = int(N[:-1])    #最後の１桁以外
    decN = int(N[-1])       #最後の1桁

    #正の数で１０で割った時の小数点以下がある時だけ、切り上げ時に＋１される
    if intN10 > 0 and decN >= 1:
        out = intN10 + 1
    else:
        out = intN10

#出力
print(out)