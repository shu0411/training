import io
import sys

_INPUT = """\
6
3 2
1 6
4 5
1 3
5 5
9 8
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_XY = [list(map(int, input().split())) for _ in range(N)]

#処理
for from_XY in list_XY:
    fartest_point = 0
    max_distance = 0
    point_no = 0
    for to_XY in list_XY:
        point_no += 1
        if from_XY == to_XY:
            continue
        distance = (from_XY[0] - to_XY[0])**2 + (from_XY[1] - to_XY[1])**2
        if max_distance < distance:
            max_distance = distance
            fartest_point = point_no
    #出力
    print(fartest_point)  
