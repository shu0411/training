import io
import sys

_INPUT = """\
10 10
7 9
4 6
6 10
2 5
5 6
5 9
6 8
4 8
1 5
1 4
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int,input().split())
list_uv = [list(map(int,input().split())) for _ in range(M)]

#処理
out = 0

list_uv.sort(key=lambda x: x[0])
list_uv.sort(key=lambda x: x[1])




#出力
print(out)