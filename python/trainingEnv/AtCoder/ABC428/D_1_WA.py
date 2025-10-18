import io
import sys

_INPUT = """\
4
4 80
183 5000
18 10
100000000 5000000000

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

import math

# 入力
T = int(input())


def count_sqrt(par_srt_begin, par_str_end):
    # 開始の平方根
    sqrt_begin = math.sqrt(int(par_srt_begin))
    int_sqrt_begin = int(sqrt_begin)

    if sqrt_begin == int_sqrt_begin:
        int_sqrt_begin -= 1

    # 終了の平方根
    sqrt_end = math.sqrt(int(par_str_end))
    int_sqrt_end = int(sqrt_end)

    tmp_count_sqrt = int_sqrt_end - int_sqrt_begin

    return tmp_count_sqrt


# 処理
for _ in range(T):
    C, D = input().split()

    left = C
    len_left = len(C)
    right_begin = str(int(C) + 1)
    len_right_begin = len(right_begin)
    right_end = str(int(C) + int(D))
    len_right_end = len(right_end)

    count = 0

    if len_right_begin == len_right_end:
        str_begin = left + right_begin
        str_end = left + right_end
        count += count_sqrt(str_begin, str_end)

    else:
        # 最小桁の計算
        str_begin = left + right_begin
        str_end = left + str(10**len_right_begin - 1)
        count += count_sqrt(str_begin, str_end)

        # 最小桁最大桁以外の計算
        if len_right_begin + 1 < len_right_end:
            for i in range(len_right_begin + 1, len_right_end):
                str_begin = left + str(10 ** (i - 1))
                str_end = left + str(10**i - 1)
                count += count_sqrt(str_begin, str_end)

        # 最大桁の計算
        str_begin = left + str(10 ** (len_right_end - 1))
        str_end = left + right_end
        count += count_sqrt(str_begin, str_end)

    # 出力
    print(count)
