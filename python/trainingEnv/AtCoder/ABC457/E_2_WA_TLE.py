import io
import sys

_INPUT = """\
4 3
1 3
1 1
2 4
4
1 4
2 4
1 3
1 1


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
for _ in range(M):
    L, R = map(int, input().split())
    dict_L_list_R[L].append(R)
    dict_R_list_L[R].append(L)

Q = int(input())

# クエリ
for _ in range(Q):
    # 入力
    S, T = map(int, input().split())

    list_R_from_S = list(filter(lambda x: x <= T, dict_L_list_R[S]))
    list_L_from_T = list(filter(lambda x: x >= S, dict_R_list_L[T]))
    len_R_from_S = len(list_R_from_S)
    len_L_from_T = len(list_L_from_T)

    # 処理
    out = "Yes"
    if len_R_from_S == 0 or len_L_from_T == 0:
        out = "No"
    else:
        max_R_from_S = max(list_R_from_S)
        min_L_from_T = min(list_L_from_T)
        if max_R_from_S < min_L_from_T:
            out = "No"
        elif (
            max_R_from_S == T
            and len_R_from_S == 1
            and min_L_from_T == S
            and len_L_from_T == 1
        ):
            out = "No"

    # 出力
    print(out)
