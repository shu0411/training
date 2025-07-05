import io
import sys

_INPUT = """\
3 2 5
1 2 9
"""
sys.stdin = io.StringIO(_INPUT)

#方針
#A:休日数、B：平日数
#list_DをA＋Bで割った余りをsetに格納
#setを順に並べたとき、1つ前の数字との差がB以上のものが1つでもあればYes
#それ以外はno

#############ここから下をコピペ#############

#入力
N,A,B = map(int, input().split())
list_D = list(map(int, input().split()))

#処理
out = "No"
W = A + B
set_D = set()
for d in list_D:
    set_D.add(d % W)

list_week_D = list(set_D)
list_week_D.sort()
for i in range(len(list_week_D)):
    if i == 0:
        continue
    if list_week_D[i] - list_week_D[i - 1] >= B+1:
        out = "Yes"
        break
if list_week_D[0]+W - list_week_D[-1] >= B+1:
    out = "Yes"

#出力
print(out)