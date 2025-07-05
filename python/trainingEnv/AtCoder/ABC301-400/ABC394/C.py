import io
import sys

_INPUT = """\
WACWA

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
list_out = []
count_W = 0
for s in S:
    if s == "W":
        count_W += 1
    else:
        if count_W == 0:
            list_out.append(s)
        else:
            if s == "A":
                list_out.append("A" + "C" * count_W)
            else:
                list_out.append("W" * count_W + s)
            count_W = 0
if count_W != 0:
    list_out.append("W" * count_W)

out = "".join(list_out)

#出力
print(out)