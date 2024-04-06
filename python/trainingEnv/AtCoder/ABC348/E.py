import io
import sys

_INPUT = """\
4
1 2
1 3
2 4
1 1 1 2
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
#関数
def dfs(v):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        if not dfs(next_v):
            return False
    return True

#入力
N = int(input())

#グラフ作成
G = [[] for _ in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

list_C = list(map(int, input().split()))

#処理
out = N

seen = [False]*N
dfs(0)





#出力
print(out)