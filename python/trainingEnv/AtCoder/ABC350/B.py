import io
import sys

_INPUT = """\
9 20
9 5 1 2 2 2 8 9 2 1 6 2 6 5 8 7 8 5 9 8
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int,input().split())
list_T = list(map(int,input().split()))

#処理
list_tooth = [1] * N
for T in list_T:
    if list_tooth[T-1] == 1:
        list_tooth[T-1] = 0
    else:
        list_tooth[T-1] = 1

out = sum(list_tooth)

#出力
print(out)