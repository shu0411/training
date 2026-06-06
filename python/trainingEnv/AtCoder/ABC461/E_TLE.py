import io
import sys

_INPUT = """\
3 5
2 2
1 1
1 3
2 2
1 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N,Q = map(int,input().split())

out = 0
set_R = set()
list_R = [0] * Q
list_C = [0] * Q
dict_last_R_idx = {}
dict_last_C_idx = {}
for i in range(Q):
    list_query = list(map(int,input().split()))
    if list_query[0] == 1:
        R = list_query[1]
        set_R.add(R)
        list_R[i] = R

        # 今回の答えの計算
        if R not in dict_last_R_idx:
            out += N
        else:
            last_idx = dict_last_R_idx[R]
            set_C_from_last = set(list_C[last_idx:i])
            out += len(set_C_from_last)-1
        
        dict_last_R_idx[R] = i

    else:
        C = list_query[1]
        list_C[i] = C
        
        # 今回の答えの計算
        if C not in dict_last_C_idx:
            out -= len(set_R)
        else:
            last_idx = dict_last_C_idx[C]
            set_R_from_last = set(list_R[last_idx:i])
            out -= len(set_R_from_last)-1

        dict_last_C_idx[C] = i

    # 出力
    print(out) 
