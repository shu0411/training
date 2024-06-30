#078
import io
import sys

_INPUT = """\
5 5
1 2
1 3
3 2
5 2
4 2
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
#入力
N,M = map(int,input().split())
#グラフの入力
G = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

#処理
out = 0
for i,g in enumerate(G):
    g.sort()
    if len(g) == 1 and g[0] < i:
        out += 1
    elif len(g) >= 2 and g[0] < i and i < g[1]:
        out += 1

#出力
print(out)