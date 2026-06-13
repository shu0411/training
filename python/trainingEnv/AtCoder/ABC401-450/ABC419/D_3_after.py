import io
import sys

_INPUT = """\
10 5
lemwrbogje
omsjbfggme
5 8
4 8
1 3
6 6
1 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int, input().split())
S = input()
T = input()

#処理
count = [0] * (N + 1)
for i in range(M):
    L, R = map(int, input().split())
    count[L-1] += 1
    count[R] -= 1

list_out = []
now = 0
for i in range(N):
    now += count[i]
    if now % 2 == 1:
        list_out.append(T[i])
    else:
        list_out.append(S[i])
    
out = "".join(list_out)

#出力
print(out)