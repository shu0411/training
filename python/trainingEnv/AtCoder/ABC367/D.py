import io
import sys

_INPUT = """\
9 5
9 9 8 2 4 4 3 5 3
"""
sys.stdin = io.StringIO(_INPUT)

#このままやるとTLEになる。
#list_Aの部分数列の中でMの倍数になるものを探す
#全探索するとO(N^2)で間に合わない
#部分数列の和を求めるときは累積和を使うと良い
#累積和を使うとO(N)で求められる
#累積和を使って部分数列の和を求めるときは、
#list_A[i:j]の和はcumsum[j] - cumsum[i]で求められる
#ただし、cumsumは累積和
#累積和を使って部分数列の和を求める
#しゃくとり法を使う
#しゃくとり法は、部分数列の和がMの倍数になるものを探すときに使える
#しゃくとり法は、O(N)で求められる

#解説のまとめ
#スタートからiまでの歩数をNで割った余りが同じ＝そこからそこまでの和がMの倍数
#→あまりの配列を作って、同じものの数を数える

#############ここから下をコピペ#############

#入力
N,M = map(int,input().split())
list_A = list(map(int,input().split()))

#処理
out = 0

#list_Aを2回繰り返す
list_A = list_A + list_A

#累積和を求める
cumsum = [0]
for i in range(N):
    cumsum.append(cumsum[-1] + list_A[i])

#しゃくとり法
i = 0
j = 0
while i < N:
    while j < 2*N and (cumsum[j] - cumsum[i]) % M != 0:
        j += 1
    out += j - i
    i += 1

#出力
print(out)