import io
import sys

_INPUT = """\
1 2
1
1 1


"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

#処理
for B in list_B:
    for A in list_A:
        if A == B:
            list_A.remove(A)
            break

#出力
print(*list_A)