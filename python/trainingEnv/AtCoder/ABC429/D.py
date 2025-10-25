import io
import sys

_INPUT = """\
5 3 2
1 2 1 0 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M, C = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
dict_place = {}
# 人がいる場所ごとの人数を記録
for item_id in list_A:
    if item_id not in dict_place:
        dict_place[item_id] = 0
    dict_place[item_id] += 1

list_items_place = sorted(dict_place.items(), key=lambda x: x[0])
# 計算用に2周目を用意。（C<=N → 2周以内にすべて終わる）
list_items_place_double = list_items_place + list_items_place

# print(list_items_place)
# print(list_items_place_double)

# 人がいる各地点から始めたときXがいくつで終わるか
list_items_place_X = []
now_count = 0
right_item_id = -1
for item_id, item_place in enumerate(list_items_place):
    while now_count < C:
        right_item_id += 1
        now_count += list_items_place_double[right_item_id][1]

    list_items_place_X.append((item_place[0], now_count))

    # 次のループの準備として計算が終わった左端の数を引く
    now_count -= item_place[1]

# 最後にM-1から始めた時のXの値が記録されていない場合、それを追加
if list_items_place_X[-1][0] != M - 1:
    while now_count < C:
        right_item_id += 1
        now_count += list_items_place_double[right_item_id][1]

    list_items_place_X.append((M - 1, now_count))

# print(list_items_place_X)

out = 0
before_place = -1
for item_place_X in list_items_place_X:
    out += item_place_X[1] * (item_place_X[0] - before_place)
    before_place = item_place_X[0]

# 出力
print(out)
