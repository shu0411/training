import io
import sys

_INPUT = """\
323132
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = input()

#処理
count_1 = 0
count_2 = 0
count_3 = 0
for n in N:
    if n == "1":
        count_1 += 1
    elif n == "2":
        count_2 += 1
    elif n == "3":
        count_3 += 1

if count_1 == 1 and count_2 == 2 and count_3 == 3:
    print("Yes")
else:
    print("No")