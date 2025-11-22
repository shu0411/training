import io
import sys

_INPUT = """\
2 11
2 42

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
    tmp_dic_rem_Ai = {x: 0 for x in range(M)}
    for A in list_A:
        rem = A * (10**i) % M
        tmp_dic_rem_Ai[rem] += 1
    list_dic_rem_Ai.append(tmp_dic_rem_Ai)

# 下の数字のあまりに応じて、足してMになる余りの個数を加算
out = 0
for A in list_A:
    rem_Aj = A % M
    rem_Ai = M - rem_Aj if rem_Aj != 0 else 0
    out += list_dic_rem_Ai[len(str(A))][rem_Ai]

# 出力
print(out)
