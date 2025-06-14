import io
import sys

_INPUT = """\
3 3
1 2 4
2 3 5
1 3 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

def dfs(graph, start, passed):
    for neighbor, weight in graph.get(start, []):
        dfs(graph, neighbor, passed)
    
#入力
N,M = map(int, input().split())
list_ABW = [list(map(int, input().split())) for _ in range(M)]
# A:始点、B:終点、W:重み
graph = {}
for a, b, w in list_ABW:
    if a not in graph:
        graph[a] = []
    graph[a].append((b, w))

#処理
out = N
passed = set()
dfs(graph, 1, passed)

#出力
print(out)