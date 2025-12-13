import io
import sys

_INPUT = """\
1000000000 4
1 1
1 101
101 1
101 101

"""
sys.stdin = io.StringIO(_INPUT)

# setを使うことで重複除外＋★集合内の検索が高速に★
#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())

# 処理
added = set()
for i in range(M):
    R, C = map(int, input().split())
    if (
        (R - 1, C - 1) not in added
        and (R - 1, C) not in added
        and (R - 1, C + 1) not in added
        and (R, C - 1) not in added
        and (R, C) not in added
        and (R, C + 1) not in added
        and (R + 1, C - 1) not in added
        and (R + 1, C) not in added
        and (R + 1, C + 1) not in added
    ):
        added.add((R, C))

# 出力
print(len(added))
