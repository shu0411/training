import io
import sys

_INPUT = """\
5 C
xoxoo
oxxoo
oxxxo
xoxxx
oxxoo

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
tmpN, X = input().split()
N = int(tmpN)
list_line = ["A", "B", "C", "D", "E"]
dict_line = {line: 0 for line in list_line}
for _ in range(N):
    S = input()
    for i, s in enumerate(list(S)):
        if s == "o":
            dict_line[list_line[i]] += 1

# 処理
out = "No"
if dict_line[X] > 0:
    out = "Yes"

# 出力
print(out)
