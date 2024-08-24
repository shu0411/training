import io
import sys

_INPUT = """\
5 3
1 2 3 4 5
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,K = map(int,input().split())
list_A = list(map(int,input().split()))

#処理
out_list = list_A[-K:] + list_A[:-K]

#出力
print(*out_list)