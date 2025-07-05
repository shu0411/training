import io
import sys

_INPUT = """\
4
1 1000000000 1000000000 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))

#処理
out = []
dict_A = {}
for i,A in enumerate(list_A):
    if A in dict_A:
        out.append(dict_A[A])
    else:
        out.append(-1)
    
    dict_A[A] = i+1

#出力
print(*out)