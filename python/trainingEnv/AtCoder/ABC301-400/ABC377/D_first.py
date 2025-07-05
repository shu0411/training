import io
import sys

_INPUT = """\
6 20
8 12
14 20
11 13
5 19
4 11
1 6
"""
sys.stdin = io.StringIO(_INPUT)

#調査
#2 3
#4 5
#→1 2のあいだで11 12 22を追加可能
#→3,4のあいだで33 34 44を追加可能
#55を追加可能

#2 2
#4 5
#1 1の間で11 を追加可能
#3 4の間で33 34 44を追加可能
#55を追加可能

#1 4 
#3 5
#→11 12 13 22 23 33
#14 15はNG
#34 44
#45 55

#############ここから下をコピペ#############

#関数定義
#範囲を入れると、その範囲内で追加可能な区間の数を返す
def addable_range(L, R):
    return (R - L + 1) * (R - L + 2) // 2

#入力
N,M = map(int, input().split())
list_LR = [list(map(int, input().split())) for _ in range(N)]

#処理
list_LR.sort()

#追加可能な区間の数を考える
out = 0
tmp_L = 1
for LR in list_LR:
    if LR[0] == LR[1]:
        if tmp_L < LR[0]:
            out += addable_range(tmp_L, LR[0] - 1)
        tmp_L = LR[1] + 1
        continue
    else:
        if tmp_L <= LR[0]:
            out += addable_range(tmp_L, LR[0])
        tmp_L = LR[1]

if tmp_L <= M:
    out += addable_range(tmp_L, M)

#出力
print(out)