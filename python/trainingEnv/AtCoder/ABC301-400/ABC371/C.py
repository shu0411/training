import io
import sys

_INPUT = """\
8
13
1 8
5 7
4 6
1 5
7 8
1 6
1 2
5 8
2 6
5 6
6 7
3 7
4 8
15
3 5
1 7
4 6
3 8
7 8
1 2
5 6
1 6
1 5
1 4
2 8
2 6
2 4
4 7
1 3
7483 1694 5868 3296 9723 5299 4326
5195 4088 5871 1384 2491 6562
1149 6326 2996 9845 7557
4041 7720 1554 5060
8329 8541 3530
4652 3874
3748
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

import itertools
#入力
N = int(input())
MG = int(input())
list_uv = [list(map(int,input().split())) for i in range(MG)]
MH = int(input())
list_ab = [list(map(int,input().split())) for i in range(MH)]
list_A = []
for i in range(N-1):
    list_A.append(list(map(int,input().split())))

#処理
out = 10 ** 6 * 28

list_N = range(1,N+1)
for v in itertools.permutations(list_N,N):
    tmp_out = 0
    list_after_uv = []
    for uv in list_uv:
        if v[uv[0]-1] > v[uv[1]-1]:
            after_uv = [v[uv[1]-1],v[uv[0]-1]]
        else:
            after_uv = [v[uv[0]-1],v[uv[1]-1]]
        list_after_uv.append(after_uv)
        if after_uv not in list_ab:
            tmp_out += list_A[after_uv[0]-1][after_uv[1]-after_uv[0]-1]
    for ab in list_ab:
        if ab not in list_after_uv:
            tmp_out += list_A[ab[0]-1][ab[1]-ab[0]-1]
    out = min(out,tmp_out)

#出力
print(out)