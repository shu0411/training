import io
import sys

_INPUT = """\
5 4
16 9 2 3 1
6 10
12 4
1 1
1000000000 1000000000

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())
list_A = list(map(int, input().split()))

list_A.sort()


# 処理
for i in range(Q):
    X, Y = map(int, input().split())
    count_a = sum((X <= i and i <= X - 1 + Y for i in list_A))
    out = X - 1 + Y
    while count_a > 0:
        out += 1
        if out not in list_A:
            count_a -= 1

    # 出力
    print(out)
