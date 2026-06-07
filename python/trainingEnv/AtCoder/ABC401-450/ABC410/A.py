import io
import sys

_INPUT = """\
15
18 89 31 2 15 93 64 78 58 19 79 59 24 50 30
38

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))
K = int(input())

#処理
out = 0
for A in list_A:
    if A >= K:
        out += 1

#出力
print(out)