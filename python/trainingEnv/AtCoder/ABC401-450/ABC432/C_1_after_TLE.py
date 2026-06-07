import io
import sys

_INPUT = """\
8 4 32
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, X, Y = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
min_A = min(list_A)
now_sum = min_A * Y  # 最小の子が全部大をもらった場合


diff_XY = Y - X

out = -1
while now_sum >= 0:
    out = 0
    for A in list_A:
        diff = A - min_A
        plus_sum = diff * Y
        # diff個増えてもmax_sumにできるか
        if plus_sum % diff_XY != 0 or plus_sum // diff_XY > A:
            break
        else:
            out += A - plus_sum // diff_XY
    else:
        break

    now_sum -= diff_XY

if now_sum < 0:
    out = -1

# 出力
print(out)
