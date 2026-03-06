import io
import sys

_INPUT = """\
10 4 100 3
1237 744 1034 759 1036 717 1121 1136 1029 899
914 1241 873 1066 958 836 746 1247 930 1307
1134 756 912 1052 1037 1347 809 875 1056 763
1081 1181 828 1251 1098 1003 1116 1152 777 1154
1049 1132 722 1140 779 1187 851 743 1062 896
1167 1081 1235 1031 1070 755 979 688 1025 936
814 884 897 944 714 731 1212 1147 943 1082
1162 1308 901 1344 971 849 744 1151 1130 951
1162 939 773 1154 1091 719 1295 1182 1197 951
900 886 1299 826 907 708 1299 788 960 1345
6 2
3 3
3 5
5 8
3 5
7 3
5 7
6 7
3 5
7 3
5 7
6 7
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
3 5
7 3
5 7
6 7
3 5
7 3
5 7
6 7
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
3 5
7 3
5 7
6 7
3 5
7 3
5 7
6 7
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M, T, U = map(int, input().split())
table_V = [list(map(int, input().split())) for _ in range(N)]
list_sxy = [tuple(map(int, input().split())) for _ in range(M)]

# 変数定義
list_txy = []
list_exy = []
table_O = []
table_L = []


# 関数
## 途中の入力値の受け取り
def get_input(param_list_txy, param_list_exy, param_table_O, param_table_L):
    param_list_txy = [tuple(map(int, input().split())) for _ in range(M)]
    param_list_exy = [tuple(map(int, input().split())) for _ in range(M)]
    param_table_O = [list(map(int, input().split())) for _ in range(N)]
    param_table_L = [list(map(int, input().split())) for _ in range(N)]
    return


# 処理
now_pos = list_sxy[0]
now_turn = 0

# 端まで移動する移動方向を決める
first_move = (0, 0)
if now_pos[0] < N // 2:
    # 上下なら上
    if now_pos[1] < N // 2:
        # 左右なら左
        if now_pos[0] <= now_pos[1]:
            first_move = (-1, 0)
        else:
            first_move = (0, -1)
    else:
        # 左右なら右
        if now_pos[0] <= now_pos[1]:
            first_move = (-1, 0)
        else:
            first_move = (0, 1)
else:
    # 上下なら下
    if now_pos[1] < N // 2:
        # 左右なら左
        if now_pos[0] <= now_pos[1]:
            first_move = (1, 0)
        else:
            first_move = (0, -1)
    else:
        # 左右なら右
        if now_pos[0] <= now_pos[1]:
            first_move = (1, 0)
        else:
            first_move = (0, 1)

# 端まで移動
while now_pos[0] > 0 and now_pos[0] < N - 1 and now_pos[1] > 0 and now_pos[1] < N - 1:
    now_pos = (now_pos[0] + first_move[0], now_pos[1] + first_move[1])
    print(now_pos[0], now_pos[1], flush=True)

    now_turn += 1
    get_input(list_txy, list_exy, table_O, table_L)


for i in range(T):

    # if first_move[0] == 0:
    # 最初に横移動した場合

    print(now_pos[0], now_pos[1], flush=True)

    now_turn += 1
    get_input(list_txy, list_exy, table_O, table_L)

    if now_turn == T:
        break
