import io
import sys

_INPUT = """\
4
ab--
--b-
---a
c---
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

def dfs(graph,  seen, v, dest):
    if v == dest:
        return "0"
    seen[v] = True
    for i in range(len(graph)):
        if graph[i][0] == v and not seen[graph[i][1]]:
            dfs(graph, graph[i][1], seen)

#入力
N = int(input())

#処理
graph = []
for i in range(N):
    A = input()
    for j in range(N):
        a = A[j]
        if a != "-":
            graph.append((i,j,a))

for i in range(N):
    out_list = []
    for j in range(N):
        if i == j:
            out_list.append("0")
            continue
        seen = [False] * N
        out_list = dfs(graph, seen, i, j)

    #出力
    print(*out_list)