import io
import sys

_INPUT = """\
5 5 416
a
aa
aaa
aa
a

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#関数：S_idを次の状態に更新する
def increment_S_id(S_id, N, K):
    if K == 1:
        ret_S_id = [S_id[0] + 1]
    else:
        partial_S_id = increment_S_id(S_id[:-1], N, K-1)
        ret_S_id = partial_S_id[:-1]
        #位上げ処理
        if partial_S_id[-1] == N:
            ret_S_id.append(0)
            ret_S_id.append(S_id[-1]+1)
        else:
            ret_S_id.append(partial_S_id[-1])
            ret_S_id.append(S_id[-1])
        
    return ret_S_id


#入力
N,K,X = map(int, input().split())
list_S = [input() for _ in range(N)]

#処理
list_connected_S = []
S_id = [0] * K
while S_id[-1] != N:
    tmp_connected_S = ""
    for i in range(K):
        tmp_connected_S += list_S[S_id[i]]
    list_connected_S.append(tmp_connected_S)

    #S_idを次の状態に更新
    S_id = increment_S_id(S_id, N, K)

list_connected_S.sort()
out = list_connected_S[X-1]

#出力
print(out)