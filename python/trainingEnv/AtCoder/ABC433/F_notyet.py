import io
import sys

_INPUT = """\
1112222334445556555

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
table_count = [[0] * len(S) for x in range(10)]
for i, s in enumerate(list(S)):
    for digit_num in range(10):
        if digit_num == s:
            table_count[digit_num][i] = table_count[digit_num][i - 1] + 1
        else:
            table_count[digit_num][i] = table_count[digit_num][i - 1]

out = 0
for i in range(len(S)):
    for digit_num in range(10):
        pass

# 出力
print(out)
