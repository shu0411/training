import io
import sys

_INPUT = """\
10000000 24

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
X,C = map(int, input().split())

#処理
out = X // (1000 + C) * 1000

#出力
print(out)