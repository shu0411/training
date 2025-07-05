import io
import sys

_INPUT = """\
2
1 2
3 4
5 6
7 8
2
1 2 2 2 1 1
2 2 1 2 1 2
"""
sys.stdin = io.StringIO(_INPUT)

#解説参照後（スマートな書き方）
#############ここから下をコピペ#############

#入力
N = int(input())

cube = [[[0]*N for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        cube[i][j] = list(map(int,input().split()))

sum_cube = [[[0]*(N+1) for i in range(N+1)] for j in range(N+1)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            sum_cube[i+1][j+1][k+1] = (sum_cube[i][j+1][k+1] 
                                        + sum_cube[i+1][j][k+1]
                                        + sum_cube[i+1][j+1][k]
                                        - sum_cube[i][j][k+1]
                                        - sum_cube[i][j+1][k]
                                        - sum_cube[i+1][j][k]
                                        + sum_cube[i][j][k]
                                        + cube[i][j][k])
print(cube)
print(sum_cube)
Q = int(input())

#処理
for i in range(Q):
    lx,rx,ly,ry,lz,rz = map(int,input().split())

    out = (sum_cube[rx][ry][rz]
        - sum_cube[lx-1][ry][rz]
        - sum_cube[rx][ly-1][rz]
        - sum_cube[rx][ry][lz-1]
        + sum_cube[lx-1][ly-1][rz]
        + sum_cube[lx-1][ry][lz-1]
        + sum_cube[rx][ly-1][lz-1]
        - sum_cube[lx-1][ly-1][lz-1])
    
    #出力
    print(out)