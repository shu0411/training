import io
import sys

_INPUT = """\
2
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

##方針
#横に見ても、縦に見ても、斜めに見ても、0→1→2となるように並べる方法。
#0と1だけ、1と2だけの数は
#★中断★

#############ここから下をコピペ#############

#入力
N = int(input())
list_S = input().split()

#処理
out = N

#出力
print(out)