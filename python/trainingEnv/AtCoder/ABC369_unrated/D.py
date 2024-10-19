import io
import sys

_INPUT = """\
5
1 5 3 2 7
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))

#処理
out = 0
next_times = 1
for i in range(N):
    if i == N-1:
        if next_times % 2 == 1:
            out += list_A[i]
        else:
            out += list_A[i] * 2
    elif i == N-2:
        if next_times % 2 == 1:
            out += list_A[i]
            next_times += 1
        elif list_A[i] * 2 >= list_A[i+1]:
            out += list_A[i] * 2
            next_times += 1
    else:
        if next_times % 2 == 1:
            if list_A[i] >= list_A[i+1] or list_A[i+1] >= list_A[i+2]:
                out += list_A[i]
                next_times += 1
        elif list_A[i] * 2 >= list_A[i+1]:
            out += list_A[i] * 2
            next_times += 1

#出力
print(out)