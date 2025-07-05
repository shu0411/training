import io
import sys

_INPUT = """\
1 1 1 1
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
list_A = list(map(int, input().split()))

#処理
out = 0
for i in range(1,5):
    if list_A.count(i) >= 2:
        out += 1
    
    if list_A.count(i) == 4:
        out += 1

#出力
print(out)