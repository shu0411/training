import io
import sys

_INPUT = """\
4
10 10 10 10
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

import collections
#入力
N = int(input())
list_A = list(map(int, input().split()))

#処理
coll_A = collections.Counter(list_A)
left = N
out = N
for i in range(N):
    # 残っている要素数から、iの要素数を引く
    left = left - coll_A[i]

    # 残っている要素数がi+1より小さい場合は、iを出力
    if left < i+1:
        out = i
        break

#出力
print(out)