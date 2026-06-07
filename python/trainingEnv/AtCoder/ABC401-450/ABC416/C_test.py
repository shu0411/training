import io
import sys

_INPUT = """\
3 2 6
abc
xxx
abc

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#関数：S_idを次の状態に更新する
#S_idはK桁の文字列で、各桁は0からN-1までの数字を表す
#前から順に0からN-1まで増やし、Nになったら次の桁を1増やす
#これを再帰的に実施
#
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

ret = increment_S_id([2, 2, 2, 2], 3, 4)
print(ret)
