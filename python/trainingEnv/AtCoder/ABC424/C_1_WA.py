import io
import sys

_INPUT = """\
6
0 0
1 3
3 2
5 5
4 6
6 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_AB = [list(map(int, input().split())) for _ in range(N)]
list_ABi = [(A,B,i+1) for i,(A,B) in enumerate(list_AB)]

#処理
skill = set()
list_ABi.sort(key=lambda x: (x[0], x[1]))
for A,B,i in list_ABi:
    if A == 0 and B == 0:
        skill.add(i)
    elif A in skill or B in skill:
        skill.add(i)

list_ABi.sort(key=lambda x: x[1])
for A,B,i in list_ABi:
    if B in skill:
        skill.add(i)

out = len(skill)

#出力
print(out)