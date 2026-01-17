import io
import sys

_INPUT = """\
13 11
defghiqsvwxyz
acejmoqrtwx
15
qhsqzhd
jcareec
wwqxqew
wxqxwex
jxxrtwa
trtqjxe
sqyggse
xxqwxew
xewwxxw
wwqxwex
xqqxqwq
qxxexxe
teqeroc
eeeqqee
vxdevyy

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
S = input()
T = input()
Q = int(input())

# 処理
list_S = list(S)
list_T = list(T)

for _ in range(Q):
    # 入力
    w = input()
    exist_S = True
    exist_T = True

    # 処理
    for char_w in w:
        if char_w not in list_S:
            exist_S = False
        if char_w not in list_T:
            exist_T = False

    out = "Unknown"
    if exist_S and not exist_T:
        out = "Takahashi"
    elif exist_T and not exist_S:
        out = "Aoki"

    # 出力
    print(out)
