import io
import sys

_INPUT = """\
10
armiearggc
ukupaunpiy
cogzmjmiob
rtwbvmtruq
qapfzsitbl
vhkihnipny
ybonzypnsn
esxvgoudra
usngxmaqpt
yfseonwhgp

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_S = [input() for _ in range(N)]

#処理
set_SS = set()
for i in range(N):
    for j in range(i + 1, N):
        set_SS.add(list_S[i] + list_S[j])
        set_SS.add(list_S[j] + list_S[i])

out = len(set_SS)

#出力
print(out)