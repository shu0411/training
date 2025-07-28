import io
import sys

_INPUT = """\
4
5
1 8 2 4 16
5
-16 24 54 81 -36
7
90000 8100 -27000 729 -300000 -2430 1000000
4
2 2 -2 -2
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T = int(input())

#処理
for i in range(T):
    N = int(input())
    list_A = list(map(int, input().split()))
    
    #処理
    out = "Yes"

    count_same = list_A.count(list_A[0])
    count_same_neg = list_A.count(-list_A[0])

    #すべて同じ数、またはすべて同じ絶対値で異符号が同数の場合は常にYesなのでスキップ
    if count_same == N:
        pass
    elif count_same + count_same_neg == N and abs( count_same - count_same_neg ) <= 1 :
        pass
    else:
        # 絶対値でソート
        sorted_A = sorted(list_A, key=lambda x: abs(x), reverse=True)
        for i in range(0, N-2):
            if sorted_A[i] * sorted_A[i + 2] != sorted_A[i + 1] ** 2:
                out = "No"
                break

    #出力
    print(out)
