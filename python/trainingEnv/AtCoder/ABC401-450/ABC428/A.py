import io
import sys

_INPUT = """\
1 1 666 428

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S, A, B, X = map(int, input().split())

# 処理
out = 0
time = 0
while time <= X:
    if time + A <= X:
        out += A * S
        time += A
    else:
        out += (X - time) * S
        break

    time += B

# 出力
print(out)
