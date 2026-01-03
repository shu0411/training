import io
import sys

_INPUT = """\
3
3
3 1
4 1
5 9
5
1000000000 1
1000000000 1
1000000000 1
1000000000 1
1000000000 1
10
133180711 458704923
531424946 225863856
141986070 637075158
500770732 289806469
502866767 408857335
559714289 569084545
287444582 992432993
559747907 753133304
432846188 949871298
727072164 756020367

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
T = int(input())

# 処理
for _ in range(T):
    # 入力
    N = int(input())

    # 処理
    total_weight = 0
    list_minus_cost = []
    for i in range(N):
        W, P = map(int, input().split())
        tmp_minus_cost = W + P
        total_weight += W
        list_minus_cost.append(tmp_minus_cost)

    list_minus_cost.sort(reverse=True)
    out = N
    for minus_cost in list_minus_cost:
        total_weight -= minus_cost
        out -= 1
        if total_weight <= 0:
            break

    # 出力
    print(out)
