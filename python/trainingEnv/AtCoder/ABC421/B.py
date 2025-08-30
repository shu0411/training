import io
import sys

_INPUT = """\
90701 90204

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
X,Y = map(int, input().split())

#処理
a_1 = X
a_2 = Y
for i in range(9):
    tmp = a_1 + a_2
    a_1 = a_2
    a_2 = int(str(tmp)[::-1])

#出力
print(a_1)