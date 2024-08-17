import io
import sys

_INPUT = """\
9 5
9 9 8 2 4 4 3 5 3
"""
sys.stdin = io.StringIO(_INPUT)

#シンプルな例
#N<=2*10^5なので、全探索は無理
#############ここから下をコピペ#############

#入力
N,M = map(int,input().split())
list_A = list(map(int,input().split()))

#処理
out = 0

#list_Aを2回繰り返す
list_A = list_A + list_A

for i in range(N):
    for j in range(N - 1):
        #i番目からi+j番目までの和がMの倍数であるかどうか
        if sum(list_A[i:i+j+1]) % M == 0:
            out += 1

#出力
print(out)