import io
import sys

_INPUT = """\
7 10
2 6
2 5
3 6
1 6
1 2
5 6
2 3
3 7
2 3
1 2
10
1 2
3 5
1 4
1 5
1 5
5 7
1 6
2 3
5 7
2 4

"""
sys.stdin = io.StringIO(_INPUT)

# 1枚目は必ず左端：L、右端：Rより小さい最大のところ。
# 2枚目は必ず右端：R、左端：上記の右端より左。
# それぞれの左端、右端から最大、最小を出す。→二分探索
#############ここから下をコピペ#############
import bisect

# 入力
N, M = map(int, input().split())
dict_L_list_R = {i: [] for i in range(1, N + 1)}
dict_R_list_L = {i: [] for i in range(1, N + 1)}
dict_count_LR = {}
dict_L_min_R = {i: 10**9 for i in range(1, N + 2)}  # 左端がiの右端の最小
dict_from_L_min_R = {i: 10**9 for i in range(1, N + 2)}  # 左端がi以上の右端の最小
for _ in range(M):
    L, R = map(int, input().split())
    dict_L_list_R[L].append(R)
    dict_R_list_L[R].append(L)

    if (L, R) not in dict_count_LR:
        dict_count_LR[(L, R)] = 0
    dict_count_LR[(L, R)] += 1

    dict_L_min_R[L] = min(dict_L_min_R[L], R)

for i in range(1, N + 1):
    dict_L_list_R[i].sort()
    dict_R_list_L[i].sort()

for i in range(N, 0, -1):
    dict_from_L_min_R[i] = min(dict_from_L_min_R[i + 1], dict_L_min_R[i])

Q = int(input())

# クエリ
for _ in range(Q):
    # 入力
    S, T = map(int, input().split())

    # 処理：(S,T)をちょうど覆う布が存在する場合
    ok = False
    if (S, T) in dict_count_LR:
        if (
            dict_count_LR[(S, T)] >= 2  # (S,T)をちょうど覆う布が2枚以上存在
            or dict_from_L_min_R[S + 1] <= T  # 左端がS+1以上、右端がT以下の布が存在
            or dict_from_L_min_R[S] <= T - 1  # 左端がS以上、右端がT-1以下の布が存在
        ):
            ok = True

        # 出力
        print("Yes" if ok else "No")
        continue

    # 処理：(S,T)をちょうど覆う布が存在しない場合

    # 左端がSで、右端がT以下の最大のindex
    list_R_from_S = dict_L_list_R[S]
    max_R_idx_from_S = bisect.bisect_right(list_R_from_S, T) - 1
    # 右端がTで、左端がS以上の最小のidx
    list_L_from_T = dict_R_list_L[T]
    min_L_idx_from_T = bisect.bisect_left(list_L_from_T, S)

    # 上記各条件を持つ布が存在し、1枚目の右端と2枚目の左端が隣り合うか重なっている
    if (
        max_R_idx_from_S >= 0
        and min_L_idx_from_T < len(list_L_from_T)
        and list_L_from_T[min_L_idx_from_T] - 1 <= list_R_from_S[max_R_idx_from_S]
    ):
        ok = True

    # 出力
    print("Yes" if ok else "No")
