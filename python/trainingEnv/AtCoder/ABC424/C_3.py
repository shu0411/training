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
dic_skill_tree = {}
got_skills = []
for i,(A,B) in enumerate(list_AB):
    if A == 0 and B == 0:
        got_skills.append(i+1)
    else:
        if A not in dic_skill_tree:
            dic_skill_tree[A] = []
        dic_skill_tree[A].append(i+1)
        if B not in dic_skill_tree:
            dic_skill_tree[B] = []
        dic_skill_tree[B].append(i+1)
dic_skill_tree = dict(sorted(dic_skill_tree.items()))

final_skills = set(got_skills)
stack = set(got_skills.copy())
while stack:
    current_skill = stack.pop()
    if current_skill in dic_skill_tree:
        for skill in dic_skill_tree[current_skill]:
            if skill not in final_skills:
                final_skills.add(skill)
                stack.add(skill)

#出力
print(len(final_skills))