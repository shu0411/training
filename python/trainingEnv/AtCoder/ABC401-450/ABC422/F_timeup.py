import io
import sys

_INPUT = """\
5 6
3 1 4 1 5
1 2
1 3
2 3
2 4
3 5
4 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int, input().split())
list_W = list(map(int, input().split()))
list_uv = [tuple(map(int, input().split())) for _ in range(M)]

list_uvw = []
for u, v in list_uv:
    list_uvw.append((u, v, list_W[v - 1]))
    list_uvw.append((v, u, list_W[u - 1]))
list_uvw.sort(key=lambda x: x[2])

#処理
fixed = [False] * N
cost = [float("inf")] * N
weight = [float("inf")] * N

def dijkstra(to, w,c):
    if fixed[to]:
        return
    fixed[to] = True
    cost[to] = min(cost[to], c)
    weight[to] = w
    for u, v, w in list_uvw:
        if u == to + 1:
            dijkstra(v - 1, w, w + c)
        elif v == to + 1:
            dijkstra(u - 1, w, w + c)

dijkstra(0, list_W[0],0)


#出力
for w in cost:
    print(w)