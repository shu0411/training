import io
import sys

_INPUT = """\
123
456
789
987
654
321
0

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
list_N = []
while True:
    N = int(input())
    list_N.append(N)
    if N == 0:
        break

#処理
#list_Nを逆順で出力
for i in range(len(list_N)):
    print(list_N[len(list_N)-i-1])
