import io
import sys

_INPUT = """\
4 4
1 1 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,L = map(int, input().split())
list_d = list(map(int, input().split()))

#処理
out = 0

if L % 3 == 0: #Lが3の倍数のとき
    dist = L // 3 #正三角形を作れる3点の間の距離
    dict_R = {0: 1} #最初の頂点は0の位置
    pos = 0
    for i in range(N-1):
        pos = (pos + list_d[i]) % L
        if pos not in dict_R:
            dict_R[pos] = 0
        dict_R[pos] += 1

    for j in range(L // 3):
        vert_1 = 0
        vert_2 = 0
        vert_3 = 0
        if j in dict_R:
            vert_1 = dict_R[j]
        if j + dist in dict_R:
            vert_2 = dict_R[j + dist]
        if j + dist * 2 in dict_R:
            vert_3 = dict_R[j + dist * 2]
        out += vert_1 * vert_2 * vert_3

#出力
print(out)