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
dic = {x: 1 for x in range(1, N+1)}
for _ in range(Q):
    X,Y = map(int,input().split())
    
    count = 0
    while min_value <= X:
        count += dic[min_value]
        dic[Y] += dic[min_value]
        min_value += 1
    
    #出力
    print(count)