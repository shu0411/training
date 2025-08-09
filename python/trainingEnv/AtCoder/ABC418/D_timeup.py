import io
import sys

_INPUT = """\
30
011011100101110111100010011010

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
T = "x" + input() + "x"

#処理
replaced_T = T.replace('x001', 'x11').replace('100x', '11x').replace('1001', '111')

out = replaced_T.count('1')

list_count_1 = []
count = 0
for i in range(len(replaced_T)):
    if replaced_T[i] == '1':
        count += 1
    else:
        list_count_1.append(count)
        count = 0

for count_1 in list_count_1:
    if count_1 > 1:
        out += count_1 * (count_1 - 1) // 2

#出力
print(out)