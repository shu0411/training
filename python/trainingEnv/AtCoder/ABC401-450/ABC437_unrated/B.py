import io
import sys

_INPUT = """\
3 5 12
78 19 70 58 83
12 30 80 20 27
48 71 8 43 82
82
30
43
8
80
70
20
78
12
71
19
48

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
H, W, N = map(int, input().split())
table_A = [input().split() for _ in range(H)]

# 処理
list_count = [0 for _ in range(H)]
for _ in range(N):
    B = input()
    for i in range(H):
        if B in table_A[i]:
            list_count[i] += 1

out = max(list_count)

# 出力
print(out)
