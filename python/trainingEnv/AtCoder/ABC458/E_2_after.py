import io
import sys

_INPUT = """\
998244 998353 998107

"""
sys.stdin = io.StringIO(_INPUT)

# 2をしきりだと思って、X2+1か所に1と3を入れていく。
# 以下3つの積
# ・X2+1か所のうち、1を入れるk箇所を選ぶ→C(X2+1, k)
# ・選んだk箇所に1を入れる→1の間（X1-1か所）にk-1個の仕切りを入れる→C(X1-1, k-1)
# ・残りのX2+1-k箇所に3を入れる（空白許可）→3（X3個）と仕切り（X2+1-k-1個）の並べ方→C(X3+X2-k, X2-k)
# nCrの計算→n!/(r! * (n-r)!) = n! * (r!)^(-1) * ((n-r)!)^(-1)
# →前計算で階乗と階乗の逆元を計算する
#############ここから下をコピペ#############

# 入力
X1, X2, X3 = map(int, input().split())

# 前処理
MOD = 998_244_353
L = 2_000_000

# 階乗
fact = [1] * (L + 1)
for i in range(1, L + 1):
    fact[i] = fact[i - 1] * i % MOD

# 階乗の逆元:x!の(MOD-2)乗のmod MOD
inv_fact = [1] * (L + 1)
inv_fact[L] = pow(fact[L], MOD - 2, MOD)
for i in range(L, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD


# 関数：C(n,r)
def binom(a, b):
    if a < b or b < 0:
        return 0
    return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD


# 処理
out = 0
for i in range(1, X2 + 1):
    tmp = binom(X2 + 1, i) * binom(X1 - 1, i - 1) * binom(X3 + X2 - i, X2 - i) % MOD
    out += tmp
    out %= MOD

# 出力
print(out)
