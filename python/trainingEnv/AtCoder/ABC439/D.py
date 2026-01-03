import io
import sys

_INPUT = """\
21
49 30 50 21 35 15 21 70 35 9 50 70 21 49 30 50 70 15 9 21 30

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))

# 処理
dict_A = {}
for i, A in enumerate(list_A):
    if A not in dict_A:
        dict_A[A] = []
    dict_A[A].append(i)

list_dict_A_items = sorted(dict_A.items(), key=lambda x: x[0])

dict_pairs_3 = {}
dict_pairs_5 = {}
dict_pairs_7 = {}
for A, list_A in list_dict_A_items:
    if A % 3 == 0:
        dict_pairs_3[A // 3] = list_A
    if A % 5 == 0 and A // 5 in dict_pairs_3:
        dict_pairs_5[A // 5] = list_A
    if A % 7 == 0 and A // 7 in dict_pairs_5:
        dict_pairs_7[A // 7] = list_A

out = 0
for key_pairs, value_7 in dict_pairs_7.items():
    list_pairs_3 = dict_pairs_3[key_pairs]
    len_list_pairs_3 = len(list_pairs_3)
    list_pairs_7 = dict_pairs_7[key_pairs]
    len_list_pairs_7 = len(list_pairs_7)

    now_3_list_idx = 0
    now_7_list_idx = 0
    count_3_lower = 0
    count_7_lower = 0
    for idx_5 in dict_pairs_5[key_pairs]:
        while (
            now_3_list_idx < len_list_pairs_3 and list_pairs_3[now_3_list_idx] < idx_5
        ):
            count_3_lower += 1
            now_3_list_idx += 1

        while (
            now_7_list_idx < len_list_pairs_7 and list_pairs_7[now_7_list_idx] < idx_5
        ):
            count_7_lower += 1
            now_7_list_idx += 1

        out += count_3_lower * count_7_lower + (
            (len_list_pairs_3 - count_3_lower) * (len_list_pairs_7 - count_7_lower)
        )

# 出力
print(out)
