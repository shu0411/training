import io
import sys

_INPUT = """\
6 7
1 1 2
1 2 3
1 3 4
1 1 5
1 5 6
3 1
2 6
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int,input().split())

#処理
#グラフの定義
G = [[] for _ in range(N)]
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        #aがbをフォローしている
        a,b = query[1],query[2]
        G[a-1].append(b-1)
    elif query[0] == 2:
        #aが自分をフォローしている人を全員フォローする(自分以外)
        a = query[1]
        for i,g in enumerate(G):
            if a-1 in g and i != a-1:
                G[a-1].append(i)
    else:
        #aが自分がフォローしている人がフォローしている人を全員フォローする
        a = query[1]
        #aがフォローしている人
        tmp_G = G[a-1].copy()
        for g in tmp_G:
            #aがフォローしている人がフォローしている人
            for gg in G[g]:
                if gg not in G[a-1] and gg != a-1:
                    G[a-1].append(gg)

#出力
for i in range(N):
    out = ""
    for j in range(N):
        if j in G[i]:
            out += "Y"
        else:
            out += "N"
    print(out)