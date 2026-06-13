import io
import sys

_INPUT = """\
6 6 3
1 3 5 100 100 100
1 1 1 1 3 5  

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M, K = map(int, input().split())
list_H = list(map(int, input().split()))
list_B = list(map(int, input().split()))

# 処理
out = "Yes"

list_H.sort()
list_B.sort()

for i in range(K):
    H = list_H[i]
    B = list_B[M - K + i]
    if H > B:
        out = "No"
        break

# 出力
print(out)
