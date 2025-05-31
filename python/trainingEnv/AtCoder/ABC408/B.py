import io
import sys

_INPUT = """\
8
19 5 5 19 5 19 4 19

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))

#処理
set_A = set(list_A)

#出力
print(len(set_A))
print(*sorted(set_A))