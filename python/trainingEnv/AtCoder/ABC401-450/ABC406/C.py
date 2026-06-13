import io
import sys

_INPUT = """\
6
1 3 6 4 2 5
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_P = list(map(int, input().split()))

#処理
tilde_count = 0
up_count = 0
before_up_count = 0
for i in range(1,N):
    if list_P[i-1] < list_P[i]:
        up_count += 1
    elif list_P[i-1] > list_P[i]:
        if up_count > 0:
            tilde_count += before_up_count * up_count
            before_up_count = up_count
            up_count = 0

if up_count > 0:
    tilde_count += before_up_count * up_count

#出力
print(tilde_count)