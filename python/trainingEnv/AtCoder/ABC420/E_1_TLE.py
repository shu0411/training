import io
import sys

_INPUT = """\
5 12
3 2
2 2
3 2
1 2 5
1 3 4
3 4
3 5
1 4 5
1 1 3
3 1
2 2
3 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())


#処理
list_Color = [False] * N #N個の頂点の色：False:白、True:黒
dic_node = {i: set([i]) for i in range(N)} #各頂点の隣接リスト
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        u,v = query[1], query[2]
        tmp_dic_node = {k: set(v) for k,v in dic_node.items()}
        for node_v in dic_node[v-1]:
            for node_u in dic_node[u-1]:
                tmp_dic_node[node_v].add(node_u)
                tmp_dic_node[node_u].add(node_v)

        dic_node = tmp_dic_node

    elif query[0] == 2:
        v = query[1]
        list_Color[v-1] = not list_Color[v-1]
    else:
        v = query[1]
        out = "No"
        for u in dic_node[v-1]:
            if list_Color[u]:
                out = "Yes"
                break

        #出力
        print(out)