import io
import sys

_INPUT = """\
8 8
185991676 311812083 311812083 84357963 185991676 185991676 724020528 369175631
455049197 387671868 4361724 724020528 724020528 455049197 455049197 724020528


"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

# 処理
list_A.sort()
list_B.sort()
list_sum_B = [0]
# 累積和
for B in list_B:
    list_sum_B.append(list_sum_B[-1] + B)

list_B.append(998244353)

out = 0
idx_B = 0
for A in list_A:
    # AがBより大きくなるBのidxを見つける
    while list_B[idx_B] <= A:
        idx_B += 1

    sum_B_to_idx_B = list_sum_B[idx_B]
    # A以下のBとの差分
    out += (A * idx_B - sum_B_to_idx_B) % 998244353
    # A以上のBとの差分
    out += ((list_sum_B[-1] - sum_B_to_idx_B) - A * (M - idx_B)) % 998244353

out %= 998244353

# 出力
print(out)
