import io
import sys

_INPUT = """\
5
1000000000 1000000000 1000000000 1000000000 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

#H=敵の体力。0以下になると敵は倒れる
#T=3の倍数で3ダメージなので、現在が3の倍数かどうかを判定し攻撃回数を決める
#T%3=1,2の時はダメージ1、T%3=0の時はダメージ3
#3回で必ず5ダメージ。
#############ここから下をコピペ#############

#入力
N = int(input())
list_H = list(map(int,input().split()))

#処理
T = 0   #攻撃回数

for H in list_H:
    division = H // 5
    remainder = H % 5
    if remainder == 0:
        T += division * 3
    else:
        if T % 3 == 0:
            #次の1回目と2回目はダメージ1、3回目はダメージ3
            if remainder <= 2:
                T += division * 3 + remainder
            else:
                T += division * 3 + 3
        elif T % 3 == 1:
            #1回目と3回目はダメージ1、2回目はダメージ3
            if remainder == 1:
                T += division * 3 + 1
            else:
                T += division * 3 + 2
        elif T % 3 == 2:
            #2回目と3回目はダメージ1、1回目はダメージ3
            if remainder <= 3:
                T += division * 3 + 1
            else:
                T += division * 3 + 2

#出力
print(T)