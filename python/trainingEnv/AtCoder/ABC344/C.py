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
#A,B,Cを昇順にソートしておく
#D以上の数は除外。
#Ｄ未満の数で総当たりして、Ａ＋Ｂ＋Ｃ＝Ｄとなる組み合わせを探す
#→TLEになる
#方針変更ABCの合計値をリストにしておいて、Dと一致するかを探す
#→TLEになる
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
list_ABC = []
for A in list_A:
    for B in list_B:
        for C in list_C:
            if A+B+C not in list_ABC:
                list_ABC.append(A+B+C)
list_ABC.sort()

#出力
for D in list_D:
    if D in list_ABC:
        print("Yes")
    else:
        print("No")