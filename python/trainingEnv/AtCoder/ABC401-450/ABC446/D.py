import io
import sys

_INPUT = """\
10
1 2 3 4 5 6 7 8 9 10

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))

# 処理
dict_len = {}
for A in list_A:
    if A - 1 in dict_len:
        dict_len[A] = dict_len[A - 1] + 1
    else:
        dict_len[A] = 1

out = max(dict_len.values())

# 出力
print(out)
