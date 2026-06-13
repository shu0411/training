import io
import sys

_INPUT = """\
5
1 2 -1 2
8 5 0 0
7 13 9 4
1 1 0 100
31 9 -74 -60

"""
sys.stdin = io.StringIO(_INPUT)

# 1マスの移動に小さいほう3回で行く方法と大きい方1回で行く方法がある。
#
#############ここから下をコピペ#############

# 入力
T = int(input())
for _ in range(T):
    out = 0
    A, B, X, Y = map(int, input().split())
    A_is_smaller = A <= B
    min_cost = min(A, B)
    max_cost = max(A, B)
    # (min_XY,min_XY)まではすべて最小で移動できる
    left_move_is_X = X >= Y
    min_XY = min(X, Y)
    out += min_XY * 2 * min_cost

    # 残りの移動に、min_cost 3回で行くか、max_cost 1回で行くか
    bigger_cost = min(min_cost * 3, max_cost)
    left_move = X + Y - min_XY * 2
    left_odd_move = (left_move + 1) // 2
    left_even_move = left_move // 2
    if left_move_is_X:
        if A_is_smaller:
            out += left_odd_move * min_cost + left_even_move * bigger_cost
        else:
            out += left_odd_move * bigger_cost + left_even_move * min_cost
    else:
        if A_is_smaller:
            out += left_odd_move * bigger_cost + left_even_move * min_cost
        else:
            out += left_odd_move * min_cost + left_even_move * bigger_cost

    # 出力
    print(out)
