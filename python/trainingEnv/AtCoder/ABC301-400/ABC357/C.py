import io
import sys

_INPUT = """\
2
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import numpy as np
#入力
N = int(input())

#処理
tmp = np.array(["#"])
if N != 0:
    for i in range(N):
        tmp_center = np.array([["."]*(3**i)]*(3**i))
        tmp = np.block([[tmp,tmp,tmp],[tmp,tmp_center,tmp],[tmp,tmp,tmp]])

#出力
for i in range(len(tmp)):
    print("".join(tmp[i]))