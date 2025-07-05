import io
import sys

_INPUT = """\
8
2 28 17 39 57 56 37 32
34 27 73 28 76 61 27
"""
sys.stdin = io.StringIO(_INPUT)

#A:おもちゃ、B:箱
#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

#処理
tmp_out = -1
list_A.sort()
list_B.sort()

for i in range(N-1, -1, -1):
    if tmp_out == -1 and list_A[i] > list_B[i-1]:
        tmp_out = list_A[i]
    elif tmp_out != -1 and list_A[i] > list_B[i]:
        print(-1)
        exit()

#出力
if tmp_out == -1:
    print(list_A[0])
else:
    print(tmp_out)