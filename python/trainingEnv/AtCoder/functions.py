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