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

out = 0
for A in list_A:
    tmp_A = 0
    tmp_B = 0
    for B in list_B:
        if A >= B:
            tmp_A += A - B
        else:
            tmp_B += B - A
    out += tmp_A % 998244353
    out += tmp_B % 998244353
    print(tmp_A % 998244353)
    print(tmp_B % 998244353)


out %= 998244353

# 出力
print(out)
