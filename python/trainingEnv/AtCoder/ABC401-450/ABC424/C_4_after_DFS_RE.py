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
    if A not in dic_skill_tree:
        dic_skill_tree[A] = []
    dic_skill_tree[A].append(i+1)
    if B not in dic_skill_tree:
        dic_skill_tree[B] = []
    dic_skill_tree[B].append(i+1)
    
#出力
skills = [False]*(N+1)

def dfs(skill):
    if skill in dic_skill_tree:
        for sub_skill in dic_skill_tree[skill]:
            if not skills[sub_skill]:
                skills[sub_skill] = True
                dfs(sub_skill)

dfs(0)

print(sum(skills))