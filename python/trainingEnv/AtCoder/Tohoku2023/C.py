import io
import sys

_INPUT = """\
6
4 2 1 5 6 3
"""
sys.stdin = io.StringIO(_INPUT)

##方針
#この順列が辞書順最小トポロジカル順序になる＝
#順番が逆になっているところは、有向辺が必ず必要な個所、それ以外はあってもなくてもいい
#有向辺が必ず必要な個所を求め、それ以外の辺の個数Nに対して2^N通りの組み合わせがある

#順番が逆になっているところ＝前の数よりも後ろの数が小さい
#############ここから下をコピペ#############

#入力
N = int(input())
list_P = input().split()

#処理
#逆順の個数を求める
before_P = 0
count = 0
for P in list_P:
    if int(P) < before_P:
        count += 1
    before_P = int(P)

#任意の辺の数に対して、2^N通りの組み合わせ
NC2 = (N*(N-1))//2
ans = 2**(NC2-count)
out = ans % 998244353

#出力
print(out)