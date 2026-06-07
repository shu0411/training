import io
import sys

_INPUT = """\
-14 14 -14 14

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
L, R, D, U = map(int, input().split())

# 処理
out = 0

# 頂点
if L <= 0 <= R and D <= 0 <= U:
    out += 1

# 軸上
x_plus = (R // 2 - max(L - 1, 0) // 2) if R > 0 and D <= 0 <= U else 0
x_minus = (-L // 2 - max(-R - 1, 0) // 2) if L < 0 and D <= 0 <= U else 0
y_plus = (U // 2 - max(D - 1, 0) // 2) if U > 0 and L <= 0 <= R else 0
y_minus = (-D // 2 - max(-U - 1, 0) // 2) if D < 0 and L <= 0 <= R else 0
out += x_plus + x_minus + y_plus + y_minus

# 軸以外
tuple_area_1 = (max(L, 0), max(R, 0), max(D, 0), max(U, 0))
tuple_area_2 = (max(-R, 0), max(-L, 0), max(D, 0), max(U, 0))
tuple_area_3 = (max(-R, 0), max(-L, 0), max(-U, 0), max(-D, 0))
tuple_area_4 = (max(L, 0), max(R, 0), max(-U, 0), max(-D, 0))
list_tuple_area = [tuple_area_1, tuple_area_2, tuple_area_3, tuple_area_4]


def cnt_rect_from_1_1(x, y):
    # (1,1)から特定の座標までの合計を返す
    # (1,1)から見て正方形部分(初項3,交差4の等差数列の和)
    square_max = min(x, y) // 2
    tmp = (4 * square_max + 2) * square_max // 2

    # 正方形以外の部分
    if x > y:
        w = x // 2 - y // 2
        h = y
    elif x < y:
        w = x
        h = y // 2 - x // 2
    else:
        w = 0
        h = 0
    tmp += w * h

    return tmp


for area in list_tuple_area:
    out += (
        cnt_rect_from_1_1(area[1], area[3])
        - cnt_rect_from_1_1(max(area[0] - 1, 0), area[3])
        - cnt_rect_from_1_1(area[1], max(area[2] - 1, 0))
        + cnt_rect_from_1_1(max(area[0] - 1, 0), max(area[2] - 1, 0))
    )


# 出力
print(out)
