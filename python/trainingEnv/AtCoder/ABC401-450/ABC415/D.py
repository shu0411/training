import io
import sys

_INPUT = """\
11 3
5 1
5 2
4 1

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
out = 0
list_ABD.sort(key=lambda x: x[2])

now_bin_count = N
for a, b, diff in list_ABD:
    if now_bin_count < a:
        continue
    #選べるAの回数
    count = (now_bin_count - a) // diff
    out += count
    now_bin_count -= count * diff

    #最後に戻ってきたBでもう一度Aを選べるか確認
    if now_bin_count >= a:
        out += 1
        now_bin_count -= diff

#出力
print(out)