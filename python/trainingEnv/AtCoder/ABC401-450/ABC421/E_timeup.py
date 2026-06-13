import io
import sys

_INPUT = """\
1 2 3 4 5 6

"""
sys.stdin = io.StringIO(_INPUT)

#５個のダイスの期待値→（１＋～＋６）＊５／６＝１７．５

#1回目の出目に対してどれを残したらどういう目になるか
#１回目の出目：6 ** 5
#どれを残すか：2 ** 5
#2回目の出目：(6-残した数) ** 5

#出目パターン：6 ** 5
#############ここから下をコピペ#############

#入力
list_A = list(map(int, input().split()))

#処理
#パターンごとの得点の計算
dict_pattern = {}
for d1 in range(1, 7):
    for d2 in range(d1, 7):
        for d3 in range(d2, 7):
            for d4 in range(d3, 7):
                for d5 in range(d4, 7):
                    dice = [d1, d2, d3, d4, d5]
                    dice.sort()
                    key = tuple(dice)
                    if key not in dict_pattern:
                        dict_dice = {}
                        for d in dice:
                            if d not in dict_dice:
                                dict_dice[d] = 0
                            dict_dice[d] += 1
                        dict_pattern[key] = dict_dice
                        max_point = 0
                        for d, c in dict_dice.items():
                            max_point =max(max_point, d * c)
                        dict_pattern[key] = max_point

#1回目の出目に対してどれを残したらどういう目になるか
p = 0  #期待値

for d1 in range(1, 7):
    for d2 in range(d1, 7):
        for d3 in range(d2, 7):
            for d4 in range(d3, 7):
                for d5 in range(d4, 7):
                    dice = [d1, d2, d3, d4, d5]
                    tmp_p = 0
                    for i in range(32):
                        new_dice = dice.copy()
                        for j in range(5):
                            if (i & (1 << j)) != 0:
                                new_dice[j] = list_A[j]
                        new_dice.sort()
                        tmp_p = max(tmp_p, dict_pattern.get(tuple(sorted(new_dice)), 0))
                    p += tmp_p

#出力
print(p)