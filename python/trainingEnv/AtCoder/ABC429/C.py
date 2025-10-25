import io
import sys

_INPUT = """\
6
3 2 5 2 2 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))

# 処理
dic_number = {}
for A in list_A:
    if A not in dic_number:
        dic_number[A] = 0
    dic_number[A] += 1

out = 0
for key, value in dic_number.items():
    if value >= 2:
        # 当該文字2つとそれ以外1つの組み合わせ
        out += value * (value - 1) // 2 * (N - value)

# 出力
print(out)
