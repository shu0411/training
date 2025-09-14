import io
import sys

_INPUT = """\
8 6
1 1 1 1 1 1 1 1
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,R = map(int, input().split())
list_L = list(map(int, input().split()))

#処理
out = 0

if list_L.count(0) == 0:
    out = 0

else:
    left = 0
    for i in range(N):
        if list_L[i] == 0:
            left = i
            break
        
    right = N - 1
    for i in range(N-1, -1, -1):
        if list_L[i] == 0:
            right = i
            break

    if R - 1 < left:
        left = R 
    
    if right < R - 1:
        right = R - 1

    out = list_L[left:right+1].count(1) + right - left + 1

#出力
print(out)