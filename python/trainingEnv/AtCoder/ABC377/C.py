import io
import sys

_INPUT = """\
20 10
1 4
7 11
7 15
8 10
11 6
12 5
13 1
15 2
20 10
20 15

"""
sys.stdin = io.StringIO(_INPUT)

#以下のマスに移動できる。
#(i+2,j+1) 
#(i+1,j+2) 
#(i−1,j+2) 
#(i−2,j+1) 
#(i−2,j−1) 
#(i−1,j−2) 
#(i+1,j−2) 
#(i+2,j−1) 

#############ここから下をコピペ#############

#入力
N, M = map(int, input().split())
list_ab = [list(map(int, input().split())) for _ in range(M)]

#処理
set_ab = set()
for ab in list_ab:
    set_ab.add(tuple(ab))
    #移動できるマスを追加
    if ab[0] <= N - 2 and ab[1] <= N - 1:
        set_ab.add((ab[0] + 2, ab[1] + 1))
    if ab[0] <= N - 1 and ab[1] <= N - 2:
        set_ab.add((ab[0] + 1, ab[1] + 2))
    if ab[0] >= 3 and ab[1] <= N - 1:
        set_ab.add((ab[0] - 2, ab[1] + 1))
    if ab[0] >= 2 and ab[1] <= N - 2:
        set_ab.add((ab[0] - 1, ab[1] + 2))
    if ab[0] >= 3 and ab[1] >= 2:
        set_ab.add((ab[0] - 2, ab[1] - 1))
    if ab[0] >= 2 and ab[1] >= 3:
        set_ab.add((ab[0] - 1, ab[1] - 2))
    if ab[0] <= N - 2 and ab[1] >= 2:
        set_ab.add((ab[0] + 2, ab[1] - 1))
    if ab[0] <= N - 1 and ab[1] >= 3:
        set_ab.add((ab[0] + 1, ab[1] - 2))

out = N * N - len(set_ab)

#出力
print(out)