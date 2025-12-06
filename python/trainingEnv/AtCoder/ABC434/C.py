import io
import sys

_INPUT = """\
3
2 5
3 1 4
8 9 11
2 6
1 1 4
3 5 8
10 36
27 37 38
30 34 54
38 20 77
45 1 36
49 38 51
52 31 58
65 43 60
71 14 42
73 36 38
85 14 29

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
T = int(input())

# 処理
for _ in range(T):
    N, H = map(int, input().split())
    out = "Yes"
    now_time = 0
    now_lowest = H
    now_highest = H
    for _ in range(N):
        t, l, u = map(int, input().split())
        if out == "Yes":
            diff = t - now_time
            # 到達可能判定
            if now_highest + diff < l or now_lowest - diff > u:
                out = "No"

        # その目標での上下限を設定
        now_time = t
        now_lowest = max(l, now_lowest - diff)
        now_highest = min(u, now_highest + diff)

    # 出力
    print(out)
