import io
import sys

_INPUT = """\
10 10
7 2620
9 2620
8 3375
1 3375
6 1395
5 1395
6 2923
10 3375
9 5929
5 1225
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,T = map(int,input().split())

#処理
#選手の得点
list_point = [0]*N
#現在の得点の一覧を作成
dic_point = {0:N}
out = 1

for i in range(T):
    A,B = map(int,input().split())

    #更新前の選手の得点を保持
    tmp = list_point[A-1]
    #選手の得点を更新
    list_point[A-1] += B

    #現在の得点の一覧を更新
    if list_point[A-1] in dic_point:
        dic_point[list_point[A-1]] += 1
    else:
        dic_point[list_point[A-1]] = 1

    #更新前の選手の得点が現在の得点の一覧にあるかどうか
    if tmp in dic_point:
        if dic_point[tmp] == 1:
            dic_point.pop(tmp)
        else:
            dic_point[tmp] -= 1

    print(len(dic_point))
