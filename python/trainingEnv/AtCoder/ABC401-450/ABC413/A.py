import io
import sys

_INPUT = """\
1 10000
100

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int, input().split())
list_A = list(map(int, input().split()))

#処理
out = "No"
sum_A = sum(list_A)
if sum_A <= M:
    out = "Yes"

#出力
print(out)