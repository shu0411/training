import io
import sys

_INPUT = """\
8 5
2 6
3 5
1 7
5 7
7 8

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int,input().split())

#処理
dic = {x: 1 for x in range(1, N+1)}
for _ in range(Q):
    X,Y = map(int,input().split())
    
    count = 0
    new_dic = dic.copy()
    for key,value in dic.items():
        if key <= X:
            count += value
            new_dic.pop(key)
        else:
            break
    
    new_dic[Y] += count
    dic = new_dic
    
    #出力
    print(count)