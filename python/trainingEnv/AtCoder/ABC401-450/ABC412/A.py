import io
import sys

_INPUT = """\
6
1 6
2 5
3 4
4 3
5 2
6 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())

#処理
out = 0

for i in range(N):
    a, b = map(int, input().split())
    #処理
    if a < b:
        out += 1

#出力
print(out)