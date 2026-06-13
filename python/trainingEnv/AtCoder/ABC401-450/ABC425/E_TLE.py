import io
import sys

_INPUT = """\
3 998244353
1
1
3
4 2 5
10
500 500 500 500 500 500 500 500 500 500

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T,M = map(int, input().split())

fac = [1] * 5001
for i in range(2, 5001):
    fac[i] = fac[i - 1] * i

#処理
for _ in range(T):
    # 入力
    N = int(input())
    list_C = list(map(int, input().split()))
    
    # 処理  
    out = 0
    sum_C = sum(list_C)
    numerator = fac[sum_C]
    denominator = 1
    for c in list_C:
        denominator *= fac[c]
    out = (numerator // denominator) % M

    # 出力
    print(out)