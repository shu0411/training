import io
import sys

_INPUT = """\
5
5 3
5 2
4 1
5 1
3 2
8
retro
chris
itchy
tuna
crab
rock
cod
ash

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_AB = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
list_S = []
dict_dict_s = {i: {j: set() for j in range(1, i + 1)} for i in range(1, 11)}
for _ in range(M):
    S = input()
    len_S = len(S)
    list_S.append(S)
    for i, s in enumerate(list(S)):
        dict_dict_s[len_S][i + 1].add(s)

# 処理
for S in list_S:
    out = "No"
    if len(S) == N:
        for i, s in enumerate(list(S)):
            A, B = list_AB[i]
            if s not in dict_dict_s[A][B]:
                break
        else:
            out = "Yes"

    # 出力
    print(out)
