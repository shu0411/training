import io
import sys

_INPUT = """\
30 10 20
11 13
30 14
6 4
7 23
30 8
17 4
6 23
24 18
26 25
9 3
18 4 36 46 28 16 34 19 37 23 25 7 24 16 17 41 24 38 6 29 10 33 38 25 47 8 13 8 42 40
2 1 9
1 8
1 9
2 20 24
2 26 18
1 20
1 26
2 24 31
1 4
2 21 27
1 25
1 29
2 10 14
2 2 19
2 15 36
2 28 6
2 13 5
1 12
1 11
2 14 43
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M,Q = map(int,input().split())

#グラフの入力
G = [[] for _ in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

list_c = list(map(int,input().split()))

#処理
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        #query[1]の色を出力
        x = query[1] - 1
        print(list_c[x])
        #query[1]の色を隣接する頂点に塗る
        for j in G[x]:
            list_c[j] = list_c[x]
    else:
        x = query[1] - 1
        y = query[2]
        #query[1]の色を出力
        print(list_c[x])
        #query[1]の色をyに変更
        list_c[x] = y
