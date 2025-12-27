import io
import sys

_INPUT = """\
10
0 305186313
1 915059758
0 105282054
1 696409999
3 185928366
3 573289179
6 254538849
3 105282054
5 696409999
8 168629803

"""
sys.stdin = io.StringIO(_INPUT)

# E 要復習：Trie木
#############ここから下をコピペ#############

# 入力
N = int(input())

# 処理
dict_list = {0: []}
for i in range(1, N + 1):
    x, y = map(int, input().split())
    tmp_list = dict_list[x].copy()
    tmp_list.append(y)
    dict_list[i] = tmp_list

sorted_list_item = sorted(dict_list.items(), key=lambda x: x[1])

# 出力
keys = []
for item in sorted_list_item[1:]:
    keys.append(item[0])
print(*keys)
