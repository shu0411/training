import io
import sys

_INPUT = """\
3
1 2 3
2
2 4
6
1 2 4 8 16 32
4
1 5 10 50
"""
sys.stdin = io.StringIO(_INPUT)

##方針
#ABCの合計値をリストにしておいて、Dと一致するかを探す
#→TLEになる
#時間後修正：listではなくsetを使う→効率化できる。
#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))
M = int(input())
list_B = list(map(int, input().split()))
L = int(input())
list_C = list(map(int, input().split()))
Q = int(input())
list_D = list(map(int, input().split()))

#処理
set_ABC = set()
for A in list_A:
    for B in list_B:
        for C in list_C:
            set_ABC.add(A + B + C)

#出力
for D in list_D:
    if D in set_ABC:
        print("Yes")
    else:
        print("No")