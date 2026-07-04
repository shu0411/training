import io
import sys

_INPUT = """\
314159265358979323846264338327950

"""
sys.stdin = io.StringIO(_INPUT)

# 500桁の1~9に対して、その桁数のその数までに各条件に当てはまる数
# A+B+C-2AB-2BC-2CA + 3ABC
#############ここから下をコピペ#############

# 入力
N = input()

# 前処理
max_digits = len(N) + 1
list_cnt = [{i: 0 for i in range(1, 9)} * max_digits]
# 3桁目の5→401~500まで
for digits in range(1, max_digits):
    for number in range(1, 10):
        count_A = (
            number * 10 ** (digits - 1) / 3 - (number - 1) * 10 ** (digits - 1) / 3
        )

        count_B = sum(list_cnt[digits - 1])
        # その桁が4の場合のみ、最上位が3のすべての数(0..0以外)を含む
        if number == 3:
            count_B += 1
        elif number == 4:
            count_B += 10 ** (digits - 1) - 1

        count_C = 0
        # 先頭はnumber-1、それ以外の2種類を加えた3種類で表現

        count_AB = 0
        count_BC = 0
        count_CA = 0
        count_ABC = 0

        tmp_count = (
            count_A
            + count_B
            + count_C
            - (count_AB + count_BC + count_CA) * 2
            + count_ABC * 3
        )
        list_cnt[digits][number] = tmp_count

# 出力
# print(out)
