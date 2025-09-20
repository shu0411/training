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

#処理
skill_tree = []
got_skills = []
for i,(A,B) in enumerate(list_AB):
    if A == 0 and B == 0:
        got_skills.append(i+1)
    else:
        skill_tree.append([A,i+1])
        skill_tree.append([B,i+1])
skill_tree.sort()

final_skills = set(got_skills)
stack = got_skills.copy()
while stack:
    current_skill = stack.pop()
    for req, skill in skill_tree:
        if req == current_skill and skill not in final_skills:
            final_skills.add(skill)
            stack.append(skill)

#出力
print(len(final_skills))