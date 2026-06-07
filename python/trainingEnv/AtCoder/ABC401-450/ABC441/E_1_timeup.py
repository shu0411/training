import io
import sys

_INPUT = """\
10
ACBBCABCAB

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
S = input()

# 処理
list_diff_AB = [0]
now_diff_AB = 0
for s in S:
    now_diff_AB = 0
    if s == "A":
        now_diff_AB = 1
    if s == "B":
        now_diff_AB = -1
    list_diff_AB.append(now_diff_AB)

print(list_diff_AB)

# 出力
