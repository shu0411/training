import io
import sys

_INPUT = """\
4 6
1 2 3 2 4 2
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
#入力
N,Q = map(int,input().split())
list_x = list(map(int,input().split()))

#処理
list_A = [0]*N
set_S = set()
for x in list_x:
    if x in set_S:
        set_S.remove(x)
    else:
        set_S.add(x)
    len_set_S = len(set_S)
    for s in set_S:
        list_A[s-1] += len_set_S

#出力
x = [str(a) for a in list_A]
print(" ".join(x))