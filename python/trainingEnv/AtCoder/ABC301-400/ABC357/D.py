import io
import sys

_INPUT = """\
9
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())

#処理
str_N = str(N)
len_N = len(str_N)
tmp_by = int("1"+ "0"*(len_N-1)+ "1")
left_N = N % 998244353
#tmp = int(str_N*N)
#out = tmp % 998244353

n = N
out = 0
#tmp_by ** N % 998244353を二分累乗法で求める
tmp_k = 1 #係数

while n > 1:
    if n % 2 == 1:
        tmp_k = tmp_k * tmp_by % 998244353
        tmp_by = tmp_by * tmp_by % 998244353
        n = (n-1) // 2 
    else:
        tmp_by = tmp_by * tmp_by % 998244353
        n = n // 2

out = (left_N * tmp_by) % 998244353

#出力
print(out)

#答えまで行けず。解説を見る。