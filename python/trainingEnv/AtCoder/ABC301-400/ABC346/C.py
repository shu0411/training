import io
import sys

_INPUT = """\
10 158260522
877914575 24979445 623690081 262703497 24979445 1822804784 1430302156 1161735902 923078537 1189330739
"""
sys.stdin = io.StringIO(_INPUT)
#N K
#A1 A2 A3 ... AN
#①1からKまでの総和を求める
#②A（重複除外）のうち、K以下の数を数える
#K - ②の数が答え
#############ここから下をコピペ#############

#入力
N, K = map(int, input().split())
list_A = list(map(int, input().split()))

#処理
#①1からKまでの総和を求める
sum_K = (1 + K) * K // 2
#②A（重複除外）のうち、K以下の数を数える
set_A = set(list_A)
sum_A = 0
for i in set_A:
    if i <= K:
        sum_A += i

#K - ②の数が答え
out = sum_K - sum_A   

#出力
print(out)