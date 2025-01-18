import io
import sys

_INPUT = """\
1000000
"""
sys.stdin = io.StringIO(_INPUT)

#0度のラインから45度のラインの間のみ検討
#中心1+0どのライン*4+45どのライン*4+内側
#############ここから下をコピペ#############

#入力
R = int(input())

#処理
out = 1

#0度のライン
out += (R-1) * 4

#45度のライン
x = R / (2 ** 0.5) #交点のX座標
out += int(x - 0.5) * 4 #角（正方形の中心+0.5）が円の中にある必要がある。-0.5で計算して切り捨てる

#内側
#円の中心から遠い方から考える
tmp_out = 0
break_flag = False
R_double = R * 2
for x in range(R-1,1,-1):
    x_double = (x+0.5) * 2
    for y in range(x-1,0,-1):
        if x_double + (y+0.5) ** 2 <= R_double:
            tmp_out += y
            if y == x-1:
                break_flag = True
            break
    if break_flag:
        tmp_out += (1 + (x-2)) * (x-2) // 2  #一番上からOKになったら、それ以降は全部OK
        break
out += tmp_out * 8

#出力
print(out)