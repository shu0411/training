import io
import sys

_INPUT = """\
8
22 L
75 L
26 R
45 R
72 R
81 R
47 L
29 R
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())

#処理
out = 0
now_L = 0
now_R = 0
for i in range(N):
    #入力
    A,S = input().split()
    
    #処理
    if S == "L":
        if now_L != 0:
            out += abs(int(A) - now_L)
        now_L = int(A)
    else:
        if now_R != 0:
            out += abs(int(A) - now_R)
        now_R = int(A)

#出力
print(out)