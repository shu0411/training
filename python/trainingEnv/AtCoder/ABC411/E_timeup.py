import io
import sys

_INPUT = """\
2
1 1 4 4 4 4
1 1 1 3 3 3
1 1 1 1 3 3

"""
sys.stdin = io.StringIO(_INPUT)

#最大値が4になる確率：4/6*1*1
#最大値が3になる確率：2/6*3/6*6/6 + 2/6*6/6*2/6

#############ここから下をコピペ#############

#aの逆元を求める(ユークリッドの互除法を使用)
def inv_euclid(a, mod):
    m0, x0, x1 = mod, 0, 1
    if mod == 1:
        return 0
    while a > 1:
        q = a // mod
        m0, mod = mod, a % mod
        x0, x1 = x1 - q * x0, x0
        a = m0
    if x1 < 0:
        x1 += m0
    return x1

#入力
N = int(input())

#処理
out_mod = 0

inv_6 = inv_euclid(6, 998244353)
inv_6_N_times = 1
for i in range(N):
    inv_6_N_times = inv_6_N_times * inv_6 % 998244353

table = []
num_set = set()
for _ in range(N):
    #入力
    list_A = list(map(int, input().split()))
    table.append(list_A)
    for num in list_A:
        num_set.add(num)

for num in num_set:
    #numが最大値になる組み合わせを求める
    count = 0
    for list_A in table:
        if num in list_A:
            count += 1

