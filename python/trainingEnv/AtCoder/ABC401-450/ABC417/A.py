import io
import sys

_INPUT = """\
20 4 8
abcdefghijklmnopqrst

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N, A, B = map(int, input().split())
S = input()

#処理
out = S[A:N-B]

#出力
print(out)