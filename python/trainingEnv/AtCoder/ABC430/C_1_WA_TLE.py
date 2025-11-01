import io
import sys

_INPUT = """\
11 4 2
abbaaabaaba

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, A, B = map(int, input().split())
S = input()

# 処理
list_count_a = [0]
list_count_b = [0]
tmp_count_a = 0
tmp_count_b = 0
for i in range(N):
    if S[i] == "a":
        tmp_count_a += 1
    else:
        tmp_count_b += 1
    list_count_a.append(tmp_count_a)
    list_count_b.append(tmp_count_b)

out_count = 0
width_count_a = 0
width_count_b = 0
for width_l in range(N + 1):
    width_r = width_l
    width_count_a_l = list_count_a[width_l]
    width_count_b_l = list_count_b[width_l]
    width_count_a = list_count_a[width_r] - width_count_a_l
    width_count_b = list_count_b[width_r] - width_count_b_l
    while width_r < N and width_count_b < B:
        if width_count_a >= A:
            out_count += 1
        width_r += 1
        width_count_a = list_count_a[width_r] - width_count_a_l
        width_count_b = list_count_b[width_r] - width_count_b_l

# 出力
print(out_count)
