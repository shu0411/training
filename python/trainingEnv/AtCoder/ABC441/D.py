import io
import sys

_INPUT = """\
2 5 3 1 100
1 1 1
2 2 100
1 2 1
1 2 1
1 2 100

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M, L, S, T = map(int, input().split())
dic_U_VC = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    U, V, C = map(int, input().split())
    dic_U_VC[U].append((V, C))

# 処理
list_now_VC = [(1, 0)]
for _ in range(L):
    list_tmp_VC = []
    for now_V, now_C in list_now_VC:
        list_next_VC = dic_U_VC[now_V]
        for next_V, next_C in list_next_VC:
            list_tmp_VC.append((next_V, now_C + next_C))
    list_now_VC = list_tmp_VC.copy()

set_out = set()
for V, C in list_now_VC:
    if V not in set_out and C >= S and C <= T:
        set_out.add(V)

list_out = sorted(list(set_out))

# 出力
print(*list_out)
