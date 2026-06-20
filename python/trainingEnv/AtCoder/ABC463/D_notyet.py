import io
import sys

_INPUT = """\
6 3
1 12
2 7
5 9
9 13
10 18
15 20

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N,K = map(int,input().split())
list_LR = [list(map(int,input().split())) for _ in range(N)]


# 処理
out = N

# 出力
print(out)
