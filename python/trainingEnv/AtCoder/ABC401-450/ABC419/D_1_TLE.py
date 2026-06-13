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
bit_change = 0b0
for i in range(M):
    L, R = map(int, input().split())
    bit_tmp = (2 ** (R - L + 1) - 1) << (N - R)
    bit_change ^= bit_tmp

str_change = ("0" * N + bin(bit_change)[2:])[-N:]

list_out = []

for i in range(N):
    if str_change[i] == "1":
        list_out.append(T[i])
    else:
        list_out.append(S[i])

out = "".join(list_out)

#出力
print(out)