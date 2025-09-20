import io
import sys

_INPUT = """\
5 4
2 1 3 3 1
2 4
1 4
1 5
3 3

"""
sys.stdin = io.StringIO(_INPUT)

#1～Nまでを1回ずつ足したものを保持。
#1-Nのときの結果を保持。

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())
list_A = list(map(int, input().split()))

list_stairs = []
for i in range(1, N+1):
    for j in range(i):
        tmp_sum = list_A[j]
    list_stairs.append(list_stairs[-1] + tmp_sum if list_stairs else tmp_sum)

list_all = []
for i in range(N):
    list_all.append(sum(list_stairs[0:i+1]))

#処理
for _ in range(Q):
    L,R = map(int, input().split())
    out = list_all[R-1] - (list_all[L-2] if L > 1 else 0)

    #出力
    print(out)