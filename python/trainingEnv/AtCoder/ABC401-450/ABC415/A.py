import io
import sys

_INPUT = """\
6
2 3 5 7 11 13
1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))
X = int(input())

#処理
out = "No"

if X in list_A:
    out = "Yes"

#出力
print(out)