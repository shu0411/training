import io
import sys

_INPUT = """\
6 20
4 6 0 3 4 2 6 5 2 3 0 3 2 5 0 3 5 0 2 0


"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())
list_X = list(map(int, input().split()))

#処理
box = [0] * N
out_list = []
for X in list_X:
    if X != 0:
        box[X - 1] += 1
        out_list.append(X)
    else:
        min_index = box.index(min(box))
        box[min_index] += 1
        out_list.append(min_index + 1)

#出力
print(*out_list)