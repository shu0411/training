import io
import sys

_INPUT = """\
6 4
R 4
L 5
L 1
R 2
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())

#処理
out = 0
now_L = 1
now_R = 2
for i in range(Q):
    H,T = input().split()
    if H == "R":
        next_R = int(T)
        tmp_next_R = next_R
        #今の位置よりも小さい場合、便宜的にNを足す
        if now_R > next_R:
            tmp_next_R += N
        #now_Rとnext_Rの間にnow_Lがある場合
        if (now_R < now_L and now_L < tmp_next_R) or (now_R < now_L+N and now_L+N < tmp_next_R):
            out += N - (tmp_next_R - now_R)
        #now_Rとnext_Rの間にnow_Lがない場合
        else:
            out += tmp_next_R - now_R
        #次のnow_Rを更新            
        now_R = next_R
    else:
        next_L = int(T)
        tmp_next_L = next_L
        #今の位置よりも小さい場合、便宜的にNを足す
        if now_L > next_L:
            tmp_next_L += N
        #now_Lとnext_Lの間にnow_Rがある場合
        if (now_L < now_R and now_R < tmp_next_L) or (now_L < now_R+N and now_R+N < tmp_next_L):
            out += N - (tmp_next_L - now_L)
        #now_Lとnext_Lの間にnow_Rがない場合
        else:
            out += tmp_next_L - now_L
        #次のnow_Lを更新
        now_L = next_L
        
#出力
print(out)