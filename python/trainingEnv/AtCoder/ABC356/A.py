import io
import sys

_INPUT = """\
10 1 10
"""
sys.stdin = io.StringIO(_INPUT)

#out 1 3 2 4 5
#順番の数列から、L番目からR番目までの数列を逆順にする
#############ここから下をコピペ#############

#入力
N,L,R = map(int,input().split())

#処理
out_list = [i for i in range(1,N+1)]
rev_list = [i for i in range(R,L-1,-1)]
out_list[L-1:R] = rev_list

#出力
print(' '.join(map(str,out_list)))