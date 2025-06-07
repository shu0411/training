import io
import sys

_INPUT = """\
4
-3 2 2 -1
1 2 2
1 3 1
1 4 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_x = list(map(int, input().split()))
list_uvw = [list(map(int, input().split())) for _ in range(N - 1)]

#処理
list_uvw.sort(key=lambda x: x[2])

out = 0
        
#出力
print(out)