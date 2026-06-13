import io
import sys

_INPUT = """\
925532735634776 8
91 40
273 265
286 153
155 126
92 83
291 228
216 90
234 9

"""
sys.stdin = io.StringIO(_INPUT)

#残りがAより大きい限り、そのAを選ぶことが可能。現在の数とAの差をdiffで割った回数分、そのAを選ぶことができる。
#diffが小さい順にソートして、選べるAを選んでいく。
#############ここから下をコピペ#############

#入力
N,M = map(int, input().split())

list_ABD = []
for i in range(M):
    a, b = map(int, input().split())
    diff = a-b
    list_ABD.append((a, b, diff))

#処理
out = N
list_ABD.sort(key=lambda x: x[2])

now_bin_count = N
for a, b, diff in list_ABD:
    if now_bin_count < a:
        continue
    #選べるAの回数
    count = (now_bin_count - a) // diff
    out += count * b
    now_bin_count -= count * diff

    #最後に戻ってきたBでもう一度Aを選べるか確認
    if now_bin_count >= a:
        out += b
        now_bin_count -= diff

#出力
print(out)