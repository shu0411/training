import io
import sys

_INPUT = """\
12
3 6 7 4 12 4 8 11 11 1 8 11
3925 9785 9752 3587 4013 1117 3937 7045 6437 6208 3391 6309
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))
list_W = list(map(int, input().split()))

#処理
out = 0
group = {}
for i,A in enumerate(list_A):
    if A not in group:
        group.setdefault(A, [])
    group[A].append(list_W[i])

for num_group in group:
    out += sum(group[num_group]) - max(group[num_group])

#出力
print(out)