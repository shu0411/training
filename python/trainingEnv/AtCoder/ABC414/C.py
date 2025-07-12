import io
import sys

_INPUT = """\
8
999999999999


"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#関数：10進数からN進数に変換
def to_base_n(s, base):
    num = int(s)
    if num == 0:
        return "0" 
    ret = ""
    while num > 0:
        ret = str(num % base) + ret
        num //= base
    return ret

#関数：N進数から10進数に変換
def from_base_n(s, base):
    ret = 0
    for i, c in enumerate(s[::-1]):
        ret += int(c) * (base ** i)
    return ret

#関数：回文かどうか
def is_palindrome(s):
    return s == s[::-1]

#入力
A = int(input())
N = int(input())

#処理
str_N = str(N)
len_N = len(str_N)

out = 0
#奇数桁の回文を作成
if len_N % 2 == 1:
    #元の数が奇数桁なので、Maxは元の数
    max_num = str_N[:(len_N + 1) // 2]
else:
    #元の数が偶数桁なので、Maxは、元の数の桁の半分まで
    max_num = 10 ** (len_N // 2) - 1
for i in range(1, int(max_num) + 1):
    #iを文字列に変換
    str_i = str(i)
    #奇数桁の回文を作成(元の数+元の数の逆のうちの一つを除く)
    palin = str_i + str_i[-2::-1]
    
    #回文をA進数に変換
    base_a = to_base_n(palin, A)
    
    #A進数が回文なら加算
    if is_palindrome(base_a):
        int_palin = int(palin)
        if int_palin <= N:
            out += int_palin

#偶数桁の回文を作成
if len_N % 2 == 0:
    #元の数が偶数桁なので、Maxは元の数
    max_num = str_N[:len_N // 2]
else:
    #元の数が奇数桁なので、Maxは、元の数の桁の半分まで
    max_num = 10 ** (len_N // 2) - 1
for i in range(1, int(max_num) + 1):
    #iを文字列に変換
    str_i = str(i)
    #偶数桁の回文を作成
    palin = str_i + str_i[::-1]

    #回文をA進数に変換
    base_a = to_base_n(palin, A)

    #A進数が回文なら加算
    if is_palindrome(base_a):
        int_palin = int(palin)
        if int_palin <= N:
            out += int_palin

#出力
print(out)