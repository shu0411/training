import io
import sys

_INPUT = """\
8
1 5
1 1
1 1
1 9
2
2
1 2
2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
Q = int(input())

#処理
list_bag = []
query = []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        list_bag.append(query[1])
    else:
        list_bag.sort(reverse=True)
        out = list_bag.pop()
        
        #出力
        print(out)