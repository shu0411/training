import io
import sys

_INPUT = """\
26
"""
sys.stdin = io.StringIO(_INPUT)

#中心1+軸上*4+内側
#時間切れ
#############ここから下をコピペ#############

#入力
R = int(input())

#処理
out = 1

#軸上
out += (R-1) * 4

#内側
tmp_out = 0
R_double = R ** 2
now_y = R-1
for x in range(1, R):
    for y in range(now_y, 0, -1):
        if (x+0.5) ** 2 + (y+0.5) ** 2 <= R_double:
            tmp_out += y
            now_y = y
            break

out += tmp_out * 4

#出力
print(out)