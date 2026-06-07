import io
import sys

_INPUT = """\
2 1 8
8 10

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, K, X = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
list_A.sort()
min_need_sake_count = 0
tmp_sake_ml = 0
tmp_sake_count = 0
out = 0
for A in list_A:
    tmp_sake_ml += A
    tmp_sake_count += 1
    if tmp_sake_ml >= X:
        min_need_sake_count = tmp_sake_count
        break
    if tmp_sake_count >= K:
        out = -1
        break
else:
    out = -1

if out != -1:
    out = N - K + min_need_sake_count

# 出力
print(out)
