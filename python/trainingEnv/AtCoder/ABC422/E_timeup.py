import io
import sys

_INPUT = """\
3
1 1
3 2
2 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_xy = [tuple(map(int, input().split())) for _ in range(N)]

#処理
out = "No"


#出力
print(out)