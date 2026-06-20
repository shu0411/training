import io
import sys

_INPUT = """\
7 7 3
1 2 1
1 3 6
2 3 4
3 5 8
3 7 4
4 5 2
4 7 9
3 1 4 1 5 9 2

"""
sys.stdin = io.StringIO(_INPUT)

# E_1からの改善点：超頂点N+1,N+2を作る
# WA理由：
# dict_edge[v]のuとvが逆。
# heapqに総時間を入れていないのでminが正しくない。
#############ここから下をコピペ#############
import heapq

# 入力
N,M,Y = map(int,input().split())
dict_edge = {i:[] for i in range(1,N+3)}
for _ in range(M):
    u,v,T = map(int,input().split())
    dict_edge[u].append((T,u,v))
    dict_edge[v].append((T,u,v))

list_X = list(map(int,input().split()))
for i,X in enumerate(list_X):
    # 頂点i+1からN+1へ
    dict_edge[i+1].append((X,i+1,N+1))
    # 頂点N+2からi+1へ
    dict_edge[N+2].append((X,N+2,i+1)) 
# 頂点N+1からN+2へ
dict_edge[N+1].append((Y,N+1,N+2))

# 処理
heapq_node = [(0,1,1)] # time,from_node,to_node
visited = set()
dict_min = {1:0}
while heapq_node:
    move_time,from_node,to_node = heapq.heappop(heapq_node)

    if to_node not in visited:
        visited.add(to_node)
        move_time = dict_min[from_node] + move_time
        
        dict_min[to_node] = move_time
        for edge in dict_edge[to_node]:
            heapq.heappush(heapq_node,edge)

# 出力
sorted_dict_min = sorted(list(dict_min.items()))
list_min = [min[1] for min in sorted_dict_min[1:N]]
print(*list_min)
