import io
import sys

_INPUT = """\
3
tea


"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
S = input()

#処理
out = "No"

if S[-3:] == "tea":
    out = "Yes"

#出力
print(out)