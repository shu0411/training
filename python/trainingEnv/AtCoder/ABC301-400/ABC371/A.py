import io
import sys

_INPUT = """\
< < <
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
AB,AC,BC = input().split()

#処理
if AB == ">":   #AB
    if AC == ">":   #ABC or ACB
        if BC == ">":   #ABC
            out = "B"
        else:   #ACB
            out = "C"
    else:   #CAB
        out = "A"
else:   #BA
    if AC == ">":   #BAC
        out = "A"
    else:   #BCA or CBA
        if BC == ">":   #BCA
            out = "C"
        else:   #CBA
            out = "B"

#出力
print(out)