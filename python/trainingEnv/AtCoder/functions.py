#便利な関数をまとめる

import time
#二分累乗法をもちいて、aのb乗を求める
def powermod(a, b, mod):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

print(powermod(99, 10000, 998244353))

#実行時間を計測する
start = time.time()  # 現在時刻（処理開始前）を取得
print(powermod(99, 10000, 998244353))
end = time.time()  # 現在時刻（処理完了後）を取得
time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
print(time_diff)  # 処理にかかった時間データを使用

#aの逆元を求める(フェルマーの小定理を使用)
def inv(a, mod):
    return powermod(a, mod - 2, mod)

for tmp in range(1, 14):
    print("tmp:" , tmp , " inv:" , inv(tmp, 13))

tmp = 3
mod = 998244353
print("tmp:" , tmp , " inv:" , inv(tmp, mod))
print("tmp:10/3 inv:" , inv(tmp, mod) * 10 % mod)

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
for tmp in range(1, 13):
    print("tmp:" , tmp , " inv_euclid:" , inv_euclid(tmp, 13))
tmp = 3
mod = 998244353
print("tmp:" , tmp , " inv_euclid:" , inv_euclid(tmp, mod))
print("tmp:10/3 inv_euclid:" , inv_euclid(tmp, mod) * 10 % mod)
