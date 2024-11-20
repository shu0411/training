import io
import sys

_INPUT = """\
AnUoHrjhgfLMcDIpzxXmEWPwBZvbKqQuiJTtFSlkNGVReOYCdsay
5
1000000000000000000 123456789 1 987654321 999999999999999999

"""
sys.stdin = io.StringIO(_INPUT)

#10^100回の操作を終えた後の S= aBAbAbaBAbaBaBAb..
#Aだけに着目すると　aAAaAaaA AaaAaAAa
#最初を0としたときの番目を2進数にしたとき、1が奇数個ならA 偶数個ならaになっている
#############ここから下をコピペ#############

#入力
S = input()
Q = int(input())
list_K = list(map(int,input().split()))

#処理
out = []
len_S = len(S)
check_S = ""
times = 0
for K in list_K:
    K -= 1
    check_S = S[K % len_S]
    times = K // len_S
    if times.bit_count() % 2 == 1:
        if check_S.islower():
            out.append(check_S.upper())
        else:
            out.append(check_S.lower())
    else:
        out.append(check_S)

#出力
print(*out)