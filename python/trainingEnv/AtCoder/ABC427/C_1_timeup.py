import io
import sys

_INPUT = """\
5 8
1 2
1 3
1 4
2 3
2 5
3 4
3 5
4 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int,input().split())
list_uv = []
for i in range(M):
    list_uv.append(list(map(int,input().split())))

#処理
out = N

#出力
print(out)