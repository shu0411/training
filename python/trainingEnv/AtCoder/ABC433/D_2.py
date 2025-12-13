import io
import sys

_INPUT = """\
12 13
80 68 862370 82217 8 56 5 168 672624 6 286057 11864

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
# 下の数字の桁数ごとに上の数字をMで割った余りを記録
list_dic_rem_Ai = [{}]
for i in range(1, 11):
    tmp_dic_rem_Ai = {}
    for A in list_A:
        rem = A * (10**i) % M
        if rem not in tmp_dic_rem_Ai:
            tmp_dic_rem_Ai[rem] = 0
        tmp_dic_rem_Ai[rem] += 1
    list_dic_rem_Ai.append(tmp_dic_rem_Ai)

# 下の数字のあまりに応じて、足してMになる余りの個数を加算
list_dic_rem_Aj = [{} for _ in range(11)]
for A in list_A:
    rem_Aj = A % M
    rem_Ai = M - rem_Aj if rem_Aj != 0 else 0
    if rem_Ai not in list_dic_rem_Aj[len(str(A))]:
        list_dic_rem_Aj[len(str(A))][rem_Ai] = 0
    list_dic_rem_Aj[len(str(A))][rem_Ai] += 1

out = 0
for i in range(1, 11):
    for j in list_dic_rem_Ai[i].keys():
        if j in list_dic_rem_Aj[i]:
            out += list_dic_rem_Ai[i][j] * list_dic_rem_Aj[i][j]

# 出力
print(out)
