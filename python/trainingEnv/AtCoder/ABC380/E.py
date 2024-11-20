import io
import sys

_INPUT = """\
5 6
1 5 4
1 4 2
2 2
1 3 2
1 2 3
2 3
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int,input().split())

#処理
list_c = [0]
list_near = [[0]]
dic = {}
for i in range(N):
    list_c.append(i+1)
    list_near.append([i+1])
    dic[i+1] = [i+1]

list_c.append(0)

for i in range(Q):
    list_S = list(map(int,input().split()))
    if list_S[0] == 1:
        x,c = list_S[1],list_S[2]
        before_c = list_c[x]

        for y in list_near[x]:
            dic[before_c].remove(y)
            list_c[y] = c
            dic[c].append(y)
        
        #隣接リストの更新
        before_near_id = min(list_near[x])-1
        after_near_id = max(list_near[x])+1
        tmp_near = list_near[x]
        if list_c[before_near_id] == c:
            tmp_near += list_near[before_near_id]
        if list_c[after_near_id] == c:
            tmp_near += list_near[after_near_id]
        for y in tmp_near:
            list_near[y] = tmp_near
        
    else:
        c = list_S[1]
        print(len(dic[c]))

#TLE