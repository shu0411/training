import io
import sys

_INPUT = """\
6
10 20 30 40 50
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))

#処理
sum_A = sum(list_A)
out = sum_A * -1

#出力
print(out)