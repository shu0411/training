import io
import sys

_INPUT = """\
6 9
6 1
1 5
2 6
2 1
3 6
4 2
6 4
3 5
5 4
"""
sys.stdin = io.StringIO(_INPUT)

#1を含む閉路があるかどうかを判定する

#############ここから下をコピペ#############
from collections import deque

#入力
N,M = map(int,input().split())
dict = {}
for _ in range(M):
    a,b = map(int,input().split())
    if a not in dict:
        dict[a] = []
    dict[a].append(b)

#処理
#頂点1を含む閉路があるかどうかを判定する
out = 1
queue = deque([1])
next_queue = deque()
visited = [False] * (N+1)
visited[1] = True
while True:
    while queue:
        v = queue.popleft()
        if v in dict:
            for u in dict[v]:
                #頂点1に到達したら終了
                if u == 1:
                    print(out)
                    exit()
                #頂点1以外で未訪問の場合、訪問済みにしてキューに追加
                if not visited[u]:
                    visited[u] = True
                    next_queue.append(u)
    
    #次に訪問する頂点がない場合、終了
    if next_queue:
        queue = next_queue
        next_queue = deque()
        out += 1
    else:
        print(-1)
        exit()

