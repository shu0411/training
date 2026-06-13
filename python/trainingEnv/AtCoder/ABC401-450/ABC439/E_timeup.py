import io
import sys

_INPUT = """\
3
3 5
1 4
2 6

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_AB = [list(map(int, input().split())) for _ in range(N)]

# 処理
out = N

# 出力
print(out)
