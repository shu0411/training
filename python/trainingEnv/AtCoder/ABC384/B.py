import io
import sys

_INPUT = """\
15 2352
2 -889
2 420
2 -275
1 957
1 -411
1 -363
1 151
2 -193
2 289
2 -770
2 109
1 345
2 551
1 -702
1 355

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,R = map(int,input().split())

#処理
div1_from = 1600
div1_to = 2799
div2_from = 1200
div2_to = 2399

out = R
for i in range(N):
    D,A = map(int,input().split())
    if D == 1 and out >= div1_from and out <= div1_to:
        out += A
    elif D == 2 and out >= div2_from and out <= div2_to:
        out += A

#出力
print(out)