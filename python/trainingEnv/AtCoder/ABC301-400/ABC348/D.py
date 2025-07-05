import io
import sys

_INPUT = """\
4 4
S...
#..#
#...
..#T
4
1 1 3
1 3 5
3 2 1
2 3 1
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
H,W = map(int, input().split())
table_A = [list(input()) for _ in range(H)]
N = int(input())
table_RCE = [list(map(int, input().split())) for _ in range(N)]

#処理
out = N

#出力
print(out)