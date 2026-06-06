import io
import sys

_INPUT = """\
5
2 4 5 1 3
4 1 5 2 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = [0] + list(map(int,input().split()))
list_B = [0] + list(map(int,input().split()))

# 処理
out = "Yes"
for i,A in enumerate(list_A):
    if list_B[A] != i:
        out = "No"
        break

# 出力
print(out)
