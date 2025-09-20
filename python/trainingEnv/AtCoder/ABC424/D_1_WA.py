import io
import sys

_INPUT = """\
2
5 5
####.
##.##
#####
.####
##.#.
2 2
..
..

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T = int(input())

#処理
for _ in range(T):
    H,W = map(int, input().split())
    list_S = [input() for _ in range(H)]

    out = 0
    list_upperleft = []

    for i in range(H-1):
        for j in range(W-1):
            if list_S[i][j] == "#" and list_S[i][j+1] == "#" and list_S[i+1][j] == "#" and list_S[i+1][j+1] == "#":
                list_upperleft.append((i,j))
    
    list_upperleft.sort(reverse=True)
    while len(list_upperleft) != 0:
        i,j = list_upperleft.pop()
        out += 1
        upperright = True
        if (i+1,j) in list_upperleft:
            list_upperleft.remove((i+1,j))
        if (i,j+1) in list_upperleft:
            list_upperleft.remove((i,j+1))
            upperright = False
        if (i+1,j+1) in list_upperleft:
            list_upperleft.remove((i+1,j+1))
            upperright = False
        if upperright and (i+1,j-1) in list_upperleft:
            list_upperleft.remove((i+1,j-1))

    #出力
    print(out)