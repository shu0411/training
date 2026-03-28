import io
import sys

_INPUT = """\
10

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

import itertools

# 入力
N = int(input())

# 処理
set_good = set()
dict_powers_two = {i: [] for i in range(1, 10)}
for i in range(30):
    power_2 = 2**i
    len_power_2 = len(str(power_2))
    dict_powers_two[len_power_2].append(power_2)

dict_digits_pairs = {}
dict_digits_pairs[1] = [[1]]
for digit in range(2, 10):
    list_next_pairs = []
    list_before_pairs = dict_digits_pairs[digit - 1]
    for pairs in list_before_pairs:
        next_pairs_append = pairs.copy()
        next_pairs_append.append(1)
        list_next_pairs.append(next_pairs_append)
        if len(pairs) == 1 or pairs[-1] < pairs[-2]:
            next_pairs_add = pairs.copy()
            next_pairs_add[-1] += 1
            list_next_pairs.append(next_pairs_add)

    dict_digits_pairs[digit] = list_next_pairs

dict_digits_numbers = {}
for digit in range(2, 10):
    list_pairs = dict_digits_pairs[digit]
    for pairs in list_pairs:
        for iter_pairs in itertools.combinations(pairs):
            while True:
                tmp_num = ""

# 出力
