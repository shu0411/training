import io
import sys

_INPUT = """\
1 3 2 4 5
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
list_A = list(map(int, input().split()))

#処理
cnt_ng = 0
cnt_ok = 0
for i in range(5):
    if list_A[i] == i or list_A[i] == i+2:
        cnt_ng += 1
    if list_A[i] == i+1:
        cnt_ok += 1

if cnt_ng == 2 and cnt_ok == 3:
    print("Yes")
else:
    print("No")
