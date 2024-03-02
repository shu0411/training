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
table_point = [[0,[i for i in range(N)]]]
out = 1

for i in range(T):
    A,B = map(int,input().split())
    tmp = list_point[A-1]
    list_point[A-1] += B
    if tmp in list_point[:A-1] or tmp in list_point[A:]:

        if list_point[A-1] in list_point[:A-1] or list_point[A-1] in list_point[A:]:
            out += 1
        else:
            out += 1
    #print(list_point)
    #print(set(list_point))
    print(len(set(list_point)))

#★辞書を使って作り直す