import io
import sys

_INPUT = """\
4 3 7
2 3 5 11
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,K,X = map(int,input().split())
list_A = list(map(int,input().split()))

#処理
out_list_A = []
out_list_A += list_A[:K]
out_list_A.append(X)
out_list_A += list_A[K:]

#出力
#out_list_Aの全要素をスペース区切りで出力
print(*out_list_A)