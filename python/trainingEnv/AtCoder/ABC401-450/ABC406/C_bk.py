import io
import sys

_INPUT = """\
12
11 3 8 9 5 2 10 4 1 6 12 7
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
#考え方間違い。A1<A2を無視している。
#入力
N = int(input())
list_P = list(map(int, input().split()))

#処理
tilde_count = 0
up_count = 0
down_count = 0
before_up_count = 0
before_down_count = 0
for i in range(1,N):
    if list_P[i-1] < list_P[i]:
        up_count += 1
        if down_count > 0:
            tilde_count += before_down_count * down_count
            before_down_count = down_count
            down_count = 0
    elif list_P[i-1] > list_P[i]:
        down_count += 1
        if up_count > 0:
            tilde_count += before_up_count * up_count
            before_up_count = up_count
            up_count = 0

if up_count > 0:
    tilde_count += before_up_count * up_count
if down_count > 0:
    tilde_count += before_down_count * down_count

#出力
print(tilde_count)