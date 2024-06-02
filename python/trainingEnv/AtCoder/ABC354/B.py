import io
import sys

_INPUT = """\
3
takahashi 2813
takahashixx 1086
takahashix 4229
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_S = []
list_C = []
for i in range(N):
    S, C = input().split()
    list_S.append(S)
    list_C.append(int(C))

#処理
sum_C = sum(list_C)
modC = sum_C % N
list_S.sort()

#出力
print(list_S[modC])