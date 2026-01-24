import io
import sys

_INPUT = """\
5 4
0 1
1 -2
1 0
-2 0
3 0
4 1
1 4
5 4
3 5

"""
sys.stdin = io.StringIO(_INPUT)

# 要復習：方向性はあっていそうだが正しい答えまでたどり着かず。順に追って確認する
#############ここから下をコピペ#############
import math

# 入力
N, Q = map(int, input().split())
list_atan = []
set_atan = set()
for i in range(1, N + 1):
    X, Y = map(int, input().split())
    atan2 = math.atan2(Y, X)
    list_atan.append(atan2)
    set_atan.add(atan2)

sorted_list_atan = sorted(list_atan)

print(list_atan)
print(sorted_list_atan)

# 処理
list_set_atan = list(set_atan)
dic_before_atan = {i: -4 for i in list_set_atan}
dic_sum_atan = {i: 0 for i in list_set_atan}
dic_sum_atan[-4] = 0
before_atan = -4
count = 0
# 180度の点の調整
atan_pi = math.atan2(0, -1)
if atan_pi in set_atan:
    count_atan_pi = sorted_list_atan.count(atan_pi)
    dic_sum_atan[-atan_pi] = sorted_list_atan.count(atan_pi)
    count = count_atan_pi
    dic_before_atan[-atan_pi] = before_atan
    before_atan = -atan_pi

for atan in sorted_list_atan:
    count += 1
    dic_sum_atan[atan] = count
    dic_before_atan[atan] = before_atan
    if atan != before_atan:
        before_atan = atan


for i in range(Q):
    # 入力
    A, B = map(int, input().split())

    # 処理
    atan_A = list_atan[A - 1]
    atan_B = list_atan[B - 1]

    if atan_A == atan_pi:
        atan_A *= -1
    if atan_B == atan_pi:
        atan_B *= -1

    print(atan_A, atan_B)

    out = 0
    before_atan_B = dic_before_atan[atan_B]
    if atan_A <= atan_B:
        # AからBまで
        out = dic_sum_atan[atan_A] - dic_sum_atan[before_atan_B]
    else:
        # Aからpiまでと-piからBまで
        out = N - dic_sum_atan[atan_A] + dic_sum_atan[before_atan_B]

    # 出力
    print(out)
