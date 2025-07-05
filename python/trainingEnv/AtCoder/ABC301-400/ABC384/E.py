import io
import sys

_INPUT = """\
3 3 2
2 2
14 6 9
4 9 20
17 15 7
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
H,W,X = map(int,input().split())
P,Q = map(int,input().split())
table_S = [list(map(int,input().split())) for _ in range(H)]

#処理
list_mine = [(P,Q)]
strength = table_S[P-1][Q-1]
table_S[P-1][Q-1] = 0
add_flg = True
while add_flg:
    add_flg = False
    tmp_list = []
    limit = strength / X
    for x,y in list_mine:
        
        #上下左右が埋まっている場合はスキップ
        #if table_S[x-1][y-1] == -1:
        #    continue

        #上下左右のマスを調べる
        #if (x+1 > H or table_S[x][y-1] == 0) \
        #and (y+1 > W or table_S[x-1][y] == 0) \
        #and (x-1 < 1 or table_S[x-2][y-1] == 0) \
        #and (y-1 < 1 or table_S[x-1][y-2] == 0):
        #    table_S[x-1][y-1] = -1
        #    continue

        #下
        if x+1 <= H and table_S[x][y-1] > 0 and table_S[x][y-1] < limit:
            tmp_list.append((x+1,y))
            strength += table_S[x][y-1]
            table_S[x][y-1] = 0
        #右
        if y+1 <= W and table_S[x-1][y] > 0 and table_S[x-1][y] < limit:
            tmp_list.append((x,y+1))
            strength += table_S[x-1][y]
            table_S[x-1][y] = 0
        #上
        if x-1 >= 1 and table_S[x-2][y-1] > 0 and table_S[x-2][y-1] < limit:
            tmp_list.append((x-1,y))
            strength += table_S[x-2][y-1]
            table_S[x-2][y-1] = 0
        #左
        if y-1 >= 1 and table_S[x-1][y-2] > 0 and table_S[x-1][y-2] < limit:
            tmp_list.append((x,y-1))
            strength += table_S[x-1][y-2]
            table_S[x-1][y-2] = 0
    
    if len(tmp_list) > 0:
        list_mine += tmp_list
        add_flg = True

#出力
print(strength)