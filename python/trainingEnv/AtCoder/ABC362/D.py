import io
import sys

_INPUT = """\
3 3
1 2 3
1 2 1
1 3 6
2 3 2
"""
sys.stdin = io.StringIO(_INPUT)
#最短経路問題→解けるようになっておく。
#https://deus-ex-machina-ism.com/?p=20917
#############ここから下をコピペ#############

#入力
N = int(input())
list_S = input().split()

#処理
out = N

#出力
print(out)