import io
import sys

_INPUT = """\
4 7
2 M
3 M
1 F
4 F
4 F
1 F
2 M
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int,input().split())

#処理
list_exist_Taro = [False] * N
for i in range(M):
    #入力
    A,B = input().split()
    #処理
    if B == "M" and not list_exist_Taro[int(A)-1]:
        list_exist_Taro[int(A)-1] = True
        #出力
        print("Yes")
    else:
        #出力
        print("No")
