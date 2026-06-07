import io
import sys

_INPUT = """\
0 0 4 2
3 2 1
R 2
D 1
U 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
Rt,Ct,Ra,Ca = map(int, input().split())
N,M,L = map(int, input().split())
list_SA = [input().split() for _ in range(M)]
list_TB = [input().split() for _ in range(L)]

#処理
list_move = []
A = 0
for SA in list_SA:
    S = SA[0]
    A += int(SA[1])
    list_move.append((A,"A", S))
B = 0
for TB in list_TB:
    T = TB[0]
    B += int(TB[1])
    list_move.append((B, "B", T))
list_move.sort()

const_move_type = {"U": (-1,0), "D": (1,0), "L": (0,-1), "R": (0,1)}

print(list_move)

out = 0
same = False
before_time = 0
if Rt == Ra and Ct == Ca:
    same = True

for move in list_move:
    time,member,dir = move
    if same:
        out += time - before_time
        before_time = time

    dx, dy = const_move_type[dir]
    if member == "A":
        Ra += dx
        Ca += dy
    else:
        Rt += dx
        Ct += dy
    if Rt == Ra and Ct == Ca:
        same = True

if same:
    out += 1

#出力
print(out)