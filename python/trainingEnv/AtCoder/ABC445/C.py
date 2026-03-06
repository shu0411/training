import io
import sys

_INPUT = """\
5
1 2 3 4 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = [0] + list(map(int, input().split()))

# 処理
list_fixed_A = list_A.copy()
for i in range(N, -1, -1):
    if list_A[i] != i:
        list_fixed_A[i] = list_fixed_A[list_A[i]]

# 出力
print(*list_fixed_A[1:])
