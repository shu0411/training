import io
import sys

_INPUT = """\
5 5
2 3 2 3 2
"""
sys.stdin = io.StringIO(_INPUT)

#答え
#1 1 2
#2 1 1
#2 1 3
#数列の和がKの倍数、かつ各要素が1以上Ri以下であるような数列を辞書順に並べている。

#方針
# 要素N個、かつ、各要素が1～Riの範囲の数列を全部作る
# その中で、和がKの倍数になっているものを抽出する
# 辞書順にする。
#############ここから下をコピペ#############

#入力
N, K = map(int, input().split())
list_R = list(map(int, input().split()))

#処理
#数列を作る関数
def make_list(in_num, input_list):
    if in_num == 0:
        return [[]]
    else:
        tmp_list = make_list(in_num-1, input_list)
        return [y + [x] for x in range(1, input_list[in_num-1]+1) for y in tmp_list]

#答えとなる数列を格納するリスト
list_ans = []
#全パターン
list_all_pattern = make_list(N, list_R)

for pattern in list_all_pattern:
    if sum(pattern) % K == 0:
        list_ans.append(pattern)

list_ans.sort()

if len(list_ans) != 0:
    for ans in list_ans:
        print(*ans)