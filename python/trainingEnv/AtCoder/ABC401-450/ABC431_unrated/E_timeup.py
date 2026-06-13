import io
import sys

_INPUT = """\
4
3 4
ABCB
CACC
BCBA
2 2
CB
AA
1 10
BCBCBCBCBC
10 10
CCAABACAAA
CCCBACACCA
BACAABCBBA
ACCCAACCCA
CCAAAACCBA
AACBBACCAA
BCCCACBBAB
CBBCAACCCC
CBBCCBCBCA
BBACABBACC

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
T = int(input())

for _ in range(T):
    H, W = map(int, input().split())

    # 処理
    out = 1

    # 出力
    print(out)
