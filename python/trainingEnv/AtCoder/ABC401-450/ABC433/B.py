import io
import sys

_INPUT = """\
6
31 9 17 10 2 9

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))

# 処理
for i, A in enumerate(list_A):
    for j in range(i, -1, -1):
        if list_A[j] > A:
            out = j + 1
            break
    else:
        out = -1

    # 出力
    print(out)
