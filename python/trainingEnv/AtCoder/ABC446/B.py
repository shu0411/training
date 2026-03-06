import io
import sys

_INPUT = """\
6 5
1
3
2
3 5
5
5 3 1 4 2
5
5 1 3 4 2
5
3 4 1 5 2
5
5 1 3 2 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())

# 処理
set_selected = set()
for i in range(N):
    # 入力
    L = int(input())
    list_X = list(map(int, input().split()))

    out = 0
    for X in list_X:
        if X not in set_selected:
            out = X
            set_selected.add(X)
            break

    # 出力
    print(out)
