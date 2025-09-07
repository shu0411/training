import io
import sys

_INPUT = """\
5
3 1 2
100 0 0
1000000 1000000 1000000
31 41 59
1000000000 10000 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T = int(input())

#処理
for _ in range(T):
    nA, nB, nC = map(int, input().split())
    min_AC = min(nA, nC)
    center = nA + nB + nC - (min_AC * 2)
    if min_AC <= center:
        out = min_AC
    else:
        center_2 = nB + (nA + nC - nB * 2) // 3
        out = min(min_AC,center_2)

    #出力
    print(out)