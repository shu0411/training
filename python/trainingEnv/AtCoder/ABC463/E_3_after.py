import io
import sys

_INPUT = """\
12 20 873
2 7 940
6 9 444
6 11 809
7 8 786
9 10 468
7 10 234
6 10 660
4 12 939
8 10 896
1 11 953
8 10 818
4 8 967
3 9 724
6 7 929
3 4 948
1 3 999
10 11 724
7 10 338
1 8 967
1 12 733
581 978 950 629 583 729 554 712 438 930 774 279

"""
sys.stdin = io.StringIO(_INPUT)

# E_1からの改善点：超頂点N+1,N+2を作る
# E_2からの改善点：
#  次のnodeに行くタイミングで次の頂点に行くまでの総時間を計算するように変更
#  上記によりfrom_nodeをheapqで管理する必要がなくなった
#############ここから下をコピペ#############
import heapq

# 入力
N,M,Y = map(int,input().split())
dict_edge = {i:[] for i in range(1,N+3)}
for _ in range(M):
    u,v,T = map(int,input().split())
    dict_edge[u].append((T,v))
    dict_edge[v].append((T,u))

list_X = list(map(int,input().split()))
for i,X in enumerate(list_X):
    # 頂点i+1からN+1へ
    dict_edge[i+1].append((X,N+1))
    # 頂点N+2からi+1へ
    dict_edge[N+2].append((X,i+1)) 
# 頂点N+1からN+2へ
dict_edge[N+1].append((Y,N+2))

# 処理
heapq_node = [(0,1)] # time,to_node
visited = set()
dict_min = {1:0}
while heapq_node:
    move_time,now_node = heapq.heappop(heapq_node)

    if now_node not in visited:
        visited.add(now_node)
        dict_min[now_node] = move_time

        for next_time,next_node in dict_edge[now_node]:
            heapq.heappush(heapq_node,(move_time + next_time,next_node))

# 出力
sorted_dict_min = sorted(list(dict_min.items()))
list_min = [min[1] for min in sorted_dict_min[1:N]]
print(*list_min)
