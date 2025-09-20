import io
import sys

_INPUT = """\
2 2 2
1 1
2 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M,K = map(int, input().split())
list_AB = [tuple(map(int, input().split())) for _ in range(K)]

#処理
out = []
dic_correct = {}
for A,B in list_AB:
    if A not in dic_correct:
        dic_correct[A] = []
    dic_correct[A].append(B)

    if len(dic_correct[A]) == M:
        out.append(A)

#出力
if len(out) != 0:
    print(*out)