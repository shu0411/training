import io
import sys

_INPUT = """\
2 2
3 2
4 1
1 3 6

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
H,W = map(int, input().split())
table_A = [list(map(int, input().split())) for _ in range(H)]
list_P = list(map(int, input().split()))

#処理
now_coin = table_A[0][0]
now_H = 0
now_W = 0
coin_list = [now_coin]
for i in range(H + W - 2):
    if now_H+1 >= H or table_A[now_H+1][now_W] < table_A[now_H][now_W+1]:
        now_coin += table_A[now_H][now_W+1]
        now_W += 1
        coin_list.append(now_coin)
    elif now_W+1 >= W or table_A[now_H][now_W+1] < table_A[now_H+1][now_W]:
        now_coin += table_A[now_H+1][now_W]
        now_H += 1
        coin_list.append(now_coin)


max_diff = 10 ** 9
for i in range(len(list_P)):
    if list_P[i] > coin_list[i+1]:
        max_diff = min(max_diff, list_P[i] - coin_list[i+1])

#出力
print(max_diff)