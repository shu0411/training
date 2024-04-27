import io
import sys

_INPUT = """\
10
eixfumagit
vtophbepfe
pxbfgsqcug
ugpugtsxzq
bvfhxyehfk
uqyfwtmglr
jaitenfqiq
acwvufpfvv
jhaddglpva
aacxsyqvoj
eixfumagit
vtophbepfe
pxbfgsqcug
ugpugtsxzq
bvfhxyehok
uqyfwtmglr
jaitenfqiq
acwvufpfvv
jhaddglpva
aacxsyqvoj
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
table_A = [input() for _ in range(N)]
table_B = [input() for _ in range(N)]

#処理
for i in range(N):
    if table_A[i] != table_B[i]:
        for j in range(N):
            if table_A[i][j] != table_B[i][j]:
                #出力
                print(i+1, j+1)
                break
