import io
import sys

_INPUT = """\
6
-87 12
-60 -54
2 38
-76 6
87 96
-17 38
"""
sys.stdin = io.StringIO(_INPUT)

#出力例
#Yes
#-66 -57 31 -6 89 9
#→Lの合計が0以下、Rの合計が0以上なら条件を満たす。
#どうやって合計が0になる組を見つけるか？
#Lの合計の絶対値が、Rの合計の絶対値より大きい場合、
#全部Lの数字にして、そこから絶対値の差の分だけ加えていく（Rまでの範囲内で）
#逆も同様。
#############ここから下をコピペ#############

#入力
N = int(input())

#処理
sum_L = 0
sum_R = 0
list_L = []
list_R = []
for i in range(N):
    L, R = list(map(int, input().split()))
    sum_L += L
    sum_R += R
    list_L.append(L)
    list_R.append(R)

#出力
if sum_L <= 0 and sum_R >= 0:
    print("Yes")
    #LRの範囲内で、合計が0になる数を探す。
    out_list = []
    diff = abs(sum_L)
    for i in range(N):
        L = list_L[i]
        R = list_R[i]
        if diff == 0:
            out_list.append(L)
        elif R-L <= diff:
            out_list.append(R)
            diff -= R-L
        else:
            out_list.append(L+diff)
            diff = 0
    print(*out_list)
    
else:
    print("No")