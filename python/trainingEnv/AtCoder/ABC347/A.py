import io
import sys

_INPUT = """\
5 10
50 51 54 60 65
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,K = map(int,input().split()) 
list_A = list(map(int,input().split()))

#処理
out = ""
for A in list_A:
    if A % K == 0:
        out += str(A//K) + " "
out = out[:-1]

#出力
print(out)