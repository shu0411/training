import io
import sys

_INPUT = """\
4
abac
bcba


"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
S = input()
T = input()

#処理
dict_S = {}
dict_T = {}
for i in range(N):
    if S[i] in dict_S:
        dict_S[S[i]].append(i)
    else:
        dict_S[S[i]] = [i]
    if T[i] in dict_T:
        dict_T[T[i]].append(i)
    else:
        dict_T[T[i]] = [i]

out = 0
checked_S = []
for i in range(N):
    if out == -1:
        break
    s = S[i]
    t = T[i]
    if s in checked_S:
        continue
    checked_S.append(s)
    list_S = dict_S[s]
    for s_index in list_S:
        if T[s_index] != t:
            out = -1
            break
    else:
        if s != t:
            out += 1

#出力
print(out)