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
# それぞれの左端、右端から最大、最小を出す。
#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
dict_L_list_R = {i: [] for i in range(1, N + 1)}
dict_R_list_L = {i: [] for i in range(1, N + 1)}
dict_L_max_R = {i: -1 for i in range(1, N + 1)}
dict_R_min_L = {i: N + 1 for i in range(1, N + 1)}
for _ in range(M):
    L, R = map(int, input().split())
    dict_L_list_R[L].append(R)
    dict_R_list_L[R].append(L)
    dict_L_max_R[L] = max(dict_L_max_R[L], R)
    dict_R_min_L[R] = min(dict_R_min_L[R], L)

Q = int(input())

# クエリ
for _ in range(Q):
    # 入力
    S, T = map(int, input().split())

    max_R_from_S = dict_L_max_R[S]
    min_L_from_T = dict_R_min_L[T]

    # 処理
    out = "Yes"
    if max_R_from_S == -1 or min_L_from_T == N + 1:
        out = "No"
    elif max_R_from_S < min_L_from_T:
        out = "No"
    elif max_R_from_S >= T:
        cnt = len(list(filter(lambda x: x <= T, dict_L_list_R[S])))
        if cnt <= 1:
            out = "No"
    elif min_L_from_T <= S:
        cnt = len(list(filter(lambda x: x >= S, dict_R_list_L[T])))
        if cnt <= 1:
            out = "No"

    # 出力
    print(out)
