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
min_value = 1
dic = {}
for _ in range(Q):
    X,Y = map(int,input().split())
    
    count = 0
    if min_value <= X:
        count = X - min_value + 1
        min_value = X + 1
    
    new_dic = dic.copy()
    list_dic_items = sorted(dic.items())
    for key,value in list_dic_items:
        if key <= X:
            count += value
            new_dic.pop(key)
        else:
            break
    
    if Y not in new_dic:
        new_dic[Y] = 0
    new_dic[Y] += count
    dic = new_dic
    
    #出力
    print(count)