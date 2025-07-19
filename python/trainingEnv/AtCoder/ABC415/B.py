import io
import sys

_INPUT = """\
.#.##..##.#.###....#
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
luggage_list = []
for i in range(len(S)):
    if S[i] == '#':
        luggage_list.append(str(i+1))

#出力
for i in range(len(luggage_list)//2):
    print(luggage_list[i*2]+","+luggage_list[i*2+1])