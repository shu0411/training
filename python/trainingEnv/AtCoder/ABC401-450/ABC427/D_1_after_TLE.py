import io
import sys

_INPUT = """\
3
4 6 2
AABB
1 2
2 3
3 1
3 3
3 4
4 2
4 6 2
ABAB
1 2
2 3
3 1
3 3
3 4
4 2
5 8 3
ABABB
1 2
2 2
2 3
3 1
3 4
4 4
4 5
5 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import queue

#入力
T = int(input())

#処理
for _ in range(T):
    out_init = ""
    #入力
    N,M,K = map(int,input().split())
    S = input()
    dic_edge = {i:[] for i in range(1,N+1) }
    count_from = [0] * (N+1) 
    for i in range(M):
        U,V = list(map(int,input().split()))
        dic_edge[U].append(V)

    #処理
    list_list_path = [[(0,1)]]
    list_before_path = [(0,1)]
    for i in range(K * 2):
        list_new_path = []
        for path in list_before_path:
            u = path[-1]
            for v in dic_edge[u]:
                list_new_path.append((u,v))
        list_before_path = list_new_path.copy()
        list_list_path.append(list_before_path)

    list_dic_node = []
    before_dic_node = {i:S[i-1] for i in range(1,N+1)}
    for list_path in list_list_path[::-1]:
        #0だったら終わり。
        if list_path[0][0] == 0:
            out_init = before_dic_node[1]
            break

        dic_node = {}
        for path in list_path:
            s = before_dic_node[path[1]]
            if path[0] not in dic_node:
                dic_node[path[0]] = s
            else:
                if s != "X"and dic_node[path[0]] != "X" and dic_node[path[0]] != s:
                    dic_node[path[0]] = "X"
        before_dic_node = dic_node
        list_dic_node.append(dic_node)

    if out_init == "A":
        out = "Alice"
    else:
        out = "Bob"

    #出力
    print(out)