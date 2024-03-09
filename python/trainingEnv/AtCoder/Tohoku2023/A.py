import io
import sys

_INPUT = """\
15
3 5 636708929
2 8 994903426
9 9 607399553
8 8 827889418
9 5 668774629
3 9 811132635
10 7 890433514
5 6 742283973
1 1 912497044
4 9 946700459
1 4 730139009
1 9 843207307
7 4 728535529
2 4 950182766
9 1 523704155
"""
sys.stdin = io.StringIO(_INPUT)

##方針
#とりあえず各座標に人口をプロット
#→プロットは不要。x、y軸が同じものを抽出して、その人口を足し合わせるだけで良い
#次のループで各町の座標で検証

#############ここから下をコピペ#############

#入力
N = int(input())

#x軸、y軸ごとの合計人口を集計する。
table_xyp = []
dic_x = {}
dic_y = {}
for i in range(N):
    x,y,p = map(int,input().split())
    table_xyp.append([x,y,p])
    if x in dic_x:
        dic_x[x] += p
    else:
        dic_x[x] = p
    if y in dic_y:
        dic_y[y] += p
    else:
        dic_y[y] = p

#処理
#各町の座標ごとに合計人口を計算。最大値を更新する
max = 0
for list_xyp in table_xyp:
    sum = dic_x[list_xyp[0]] + dic_y[list_xyp[1]] - list_xyp[2]
    if sum > max:
        max = sum

#出力
print(max)