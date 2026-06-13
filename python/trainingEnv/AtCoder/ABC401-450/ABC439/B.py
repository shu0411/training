import io
import sys

_INPUT = """\
2026
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())

# 処理
check_num = N
list_exist = [N]
out = "Yes"
while check_num != 1:
    str_check_num = str(check_num)
    tmp_num = 0
    for digit in list(str_check_num):
        tmp_num += int(digit) ** 2
    if tmp_num in list_exist:
        out = "No"
        break

    list_exist.append(tmp_num)
    check_num = tmp_num

# 出力
print(out)
