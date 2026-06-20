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

# 例が正解にならず。
# Xの訪問済み、未訪問を管理しようとした結果、普通に移動したときの状態を管理しきれていない。
# そもそもそれを分けない方法を考えるべきだった。
#############ここから下をコピペ#############
import heapq

heapq_not_visited_X = [] 
heapq_visited_X = []

def warp():
    visit_X = heapq.heappop(heapq_not_visited_X)
    heapq.heappush(heapq_visited_X,visit_X)

# 入力
N,M,Y = map(int,input().split())
dict_edge = {i:[] for i in range(1,N+1)}
for _ in range(M):
    u,v,T = map(int,input().split())
    dict_edge[u].append((T,u,v))
    dict_edge[v].append((T,u,v))

list_X = list(map(int,input().split()))
heapq_not_visited_X = [(x,i+2) for i,x in enumerate(list_X[1:])]
heapq.heapify(heapq_not_visited_X)
heapq_visited_X = [(list_X[0],1)]

# 処理
heapq_node = [(0,1,1)] # time,from_node,to_node
visited = []
dict_min = {1:0}
while heapq_node:
    move_time,from_node,to_node = heapq.heappop(heapq_node)

    if to_node not in visited:
        visited.append(to_node)
        move_time = dict_min[from_node] + move_time

        #その時点のワープの最短
        warp_time_X1,warp_from = heapq_visited_X[0]
        warp_time_X2,warp_to = heapq_not_visited_X[0]
        warp_time = dict_min[warp_from] + warp_time_X1 + warp_time_X2 + Y
        
        
        if move_time < warp_time:
            # 移動を選択
            dict_min[to_node] = move_time
            for edge in dict_edge[to_node]:
                heapq.heappush(heapq_node,edge)
                heapq.heappush()
        else:
            # ワープを選択
            dict_min[to_node] = warp_time
            warp()
            for edge in dict_edge[warp_to]:
                heapq.heappush(heapq_node,edge)
    
    if len(heapq_node) == 0 and len(visited) < N:
        warp_time_X1,warp_from = heapq_visited_X[0]
        warp_time_X2,warp_to = heapq_not_visited_X[0]
        warp_time = dict_min[warp_from] + warp_time_X1 + warp_time_X2 + Y
        dict_min[to_node] = warp_time
        warp()
        for edge in dict_edge[warp_to]:
            heapq.heappush(heapq_node,edge)


# 出力
print(*list(dict_min.values())[1:])
    
