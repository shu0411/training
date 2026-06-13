import io
import sys

_INPUT = """\
3
5
1 8 2 4 16
5
-16 24 54 81 -36
7
90000 8100 -27000 729 -300000 -2430 1000000
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

    sorted_A = sorted(list_A)
    if sorted_A[0] < 0 and sorted_A[-1] > 0:
        
        if sorted_A[N // 2] > 0:
            # 中央が正の数の場合、等比数列の最初は正の数
            for j in range(0, N // 2):
                if sorted_A[(j + 1) * (-1)] * sorted_A[(j + 2) * (-1)] != sorted_A[j] ** 2:
                    out = "No"
                    break
        else:
            # 中央が負の数の場合、等比数列の最初は負の数
            times = sorted_A[-1] / sorted_A[0]
            for j in range(0, N // 2):
                if sorted_A[j] * sorted_A[j + 1] != sorted_A[(j + 1) * (-1)] ** 2:
                    out = "No"
                    break
    else:
        for j in range(N - 2):
            if sorted_A[j] * sorted_A[j + 2] != sorted_A[j + 1] ** 2:
                out = "No"
                break

    #出力
    print(out)
