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

#AC(時間切れ)ただし、変数の定義の仕方によって、もっとスマートに書ける
#############ここから下をコピペ#############

#入力
N = int(input())
sum_cube = []
tmp_sum_layer = []
tmp_sum_list = [0]*N
tmp_list = []
for i in range(N):
    tmp_sum_layer = []
    if i == 0:
        #1層目
        for j in range(N):
            tmp_sum_list = [0]*N
            if j == 0:
                tmp_list = list(map(int,input().split()))
                for k in range(N):
                    if k == 0:
                        tmp_sum_list[k] = tmp_list[k]
                    else:
                        tmp_sum_list[k] = tmp_sum_list[k-1] + tmp_list[k]
                tmp_sum_layer.append(tmp_sum_list)
            else:        
                tmp_list = list(map(int,input().split()))
                for k in range(N):
                    if k == 0:
                        tmp_sum_list[k] = tmp_sum_layer[j-1][k] + tmp_list[k]
                    else:
                        tmp_sum_list[k] = tmp_sum_layer[j-1][k] - tmp_sum_layer[j-1][k-1] + tmp_sum_list[k-1] + tmp_list[k]
                tmp_sum_layer.append(tmp_sum_list)
    else:
        for j in range(N):
            tmp_sum_list = [0]*N
            if j == 0:
                tmp_list = list(map(int,input().split()))
                for k in range(N):
                    if k == 0:
                        tmp_sum_list[k] = sum_cube[i-1][j][k] + tmp_list[k]
                    else:
                        tmp_sum_list[k] = sum_cube[i-1][j][k] + (tmp_sum_list[k-1] - sum_cube[i-1][j][k-1]) + tmp_list[k]
                    
            else:
                tmp_list = list(map(int,input().split()))
                for k in range(N):
                    if k == 0:
                        tmp_sum_list[k] = sum_cube[i-1][j][k] + (tmp_sum_layer[j-1][k] - sum_cube[i-1][j-1][k]) + tmp_list[k]
                    else:
                        tmp_sum_list[k] = sum_cube[i-1][j][k] + (tmp_sum_layer[j-1][k] - sum_cube[i-1][j-1][k]) + (tmp_sum_list[k-1] - sum_cube[i-1][j][k-1] - (tmp_sum_layer[j-1][k-1] - sum_cube[i-1][j-1][k-1])) + tmp_list[k]
            tmp_sum_layer.append(tmp_sum_list)
    sum_cube.append(tmp_sum_layer)    
    
Q = int(input())

#処理
for i in range(Q):
    tmp_lx,tmp_rx,tmp_ly,tmp_ry,tmp_lz,tmp_rz = map(int,input().split())
    lx = tmp_lx - 1
    rx = tmp_rx - 1
    ly = tmp_ly - 1
    ry = tmp_ry - 1
    lz = tmp_lz - 1
    rz = tmp_rz - 1

    max = sum_cube[rx][ry][rz]
    minus_z = sum_cube[lx-1][ry][rz] if lx > 0 else 0
    minus_y = (sum_cube[rx][ly-1][rz] if ly > 0 else 0) - (sum_cube[lx-1][ly-1][rz] if lx > 0 and ly > 0 else 0)
    minus_x = (sum_cube[rx][ry][lz-1] if lz > 0 else 0) - (sum_cube[rx][ly-1][lz-1] if ly > 0 and lz > 0 else 0) - (sum_cube[lx-1][ry][lz-1] if lx > 0 and lz > 0 else 0) + (sum_cube[lx-1][ly-1][lz-1] if lx > 0 and ly > 0 and lz > 0 else 0)

    out = max - minus_z - minus_y - minus_x
    #出力
    print(out)