import io
import sys

_INPUT = """\
5 2
7 13 3 99 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,K = map(int, input().split())
list_A = list(map(int, input().split()))

#処理
ans = 1
for A in list_A:
    ans *= A
    if len(str(ans)) > K:
        ans = 1

#出力
print(ans)