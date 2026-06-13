import io
import sys

_INPUT = """\
7 1023
"""
sys.stdin = io.StringIO(_INPUT)
#    1 5 3 7 2 6 4 8
#    0 1 2 3 4 5 6 7
#60→ 8 7 8 7 8 7 8 7
#59→ 8 7 8 7 8 7 7 7
# 000
# 100
# 010
# 110
# 001
# 101
# 011
# 111
#############ここから下をコピペ#############

#入力
N,K = map(int, input().split())

#処理
base = K // (2 ** N)
left = K % (2 ** N)

list_B = [base] * (2 ** N)

if left == 0:
    U = 0
else:
    U = 1
    for i in range(left):
        bit = bin(i)[2:].zfill(N)
        rev_bit = bit[::-1]
        idx = int(rev_bit, 2)
        list_B[idx] += 1

#出力
print(U)
print(" ".join(map(str, list_B)))
