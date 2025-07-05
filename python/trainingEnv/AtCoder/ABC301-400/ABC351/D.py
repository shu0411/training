import io
import sys

_INPUT = """\
3 3
.##
#..
...
"""
sys.stdin = io.StringIO(_INPUT)
#(問題整理)
#H*Wのマス目があり、各マスには#か.が書かれている
#H,Wは1以上1000以下
#.=何もない、#=磁石
#磁石が上下左右にあると移動できなくなる
#任意のマスから始めて到達できるマスの最大値を求める
#(方針)
#磁石の上下左右をxに変換
#.がない場合、移動可能なマスの最大値は1
#.がある場合、そこから始めて、到達可能なマスの数を数える
#############ここから下をコピペ#############

#深さ優先探索関数
def dfs(x, y):
    if [x, y] not in list_place:
        #到達したマスの座標をlist_placeに追加
        list_place.append([x, y])
        #.x判定
        #上
        if x > 0:
            if table_S[x-1][y] == ".":
                dfs(x-1, y)
            elif table_S[x-1][y] == "x" and [x-1, y] not in list_place:
                list_place.append([x-1, y])
        #下
        if x < H-1:
            if table_S[x+1][y] == ".":
                dfs(x+1, y)
            elif table_S[x+1][y] == "x" and [x+1, y] not in list_place:
                list_place.append([x+1, y])
        #左
        if y > 0:
            if table_S[x][y-1] == ".":
                dfs(x, y-1)
            elif table_S[x][y-1] == "x" and [x, y-1] not in list_place:
                list_place.append([x, y-1])
        #右
        if y < W-1:
            if table_S[x][y+1] == ".":
                dfs(x, y+1)
            elif table_S[x][y+1] == "x" and [x, y+1] not in list_place:
                list_place.append([x, y+1])

#入力
H,W = map(int, input().split())
table_S = [list(input()) for _ in range(H)]

#処理
#磁石の上下左右をxに変換
for i in range(H):
    for j in range(W):
        if table_S[i][j] == "#":
            #上
            if i > 0 and table_S[i-1][j] == ".":
                    table_S[i-1][j] = "x"
            #下
            if i < H-1 and table_S[i+1][j] == ".":
                    table_S[i+1][j] = "x"
            #左
            if j > 0 and table_S[i][j-1] == ".":
                    table_S[i][j-1] = "x"
            #右
            if j < W-1 and table_S[i][j+1] == ".":
                    table_S[i][j+1] = "x"

#空白がない場合
if all([all([s == "x" or s == "#" for s in row]) for row in table_S]):
    print(1)
    exit()

#空白がある場合、深さ優先探索で到達可能なマスの数を数える
out = 0
list_place = []
for i in range(H):
    for j in range(W):
        if table_S[i][j] == ".":
            list_place = []
            dfs(i, j)
            out = max(len(list_place),out)
            
#出力
print(out)

#54中、TLE8、RE18、あとはAC