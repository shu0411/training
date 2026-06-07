import io
import sys

_INPUT = """\
6
g 4
j 1
m 4
e 4
d 3
i 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())

#処理
out = ""
cnt = 0
for i in range(N):
    c,l = input().split()
    l = int(l)
    if cnt + l <= 100:
        out += c * l
        cnt += l
    else:
        out = "Too Long"
        break

#出力
print(out)