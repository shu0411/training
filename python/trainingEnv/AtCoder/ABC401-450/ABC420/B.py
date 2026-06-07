import io
import sys

_INPUT = """\
7 8
11010011
01000000
01111100
10111000
10011110
10100101
10010110

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int, input().split())
list_S = [input() for _ in range(N)]

#処理
point = [0] * N
for i in range(M):
    dic_vote = {"0":[],"1":[]}
    winner = ""
    for j in range(N):
        dic_vote[list_S[j][i]].append(j)

    if len(dic_vote["0"]) == 0:
        winner = "1"
    elif len(dic_vote["1"]) == 0:
        winner = "0"
    elif len(dic_vote["0"]) < len(dic_vote["1"]):
        winner = "0"
    else:
        winner = "1"
        
    for member in dic_vote[winner]:
        point[member] += 1

max_point = max(point)
winner_list = []
for i in range(N):
    if point[i] == max_point:
        winner_list.append(i+1)

#出力
print(*winner_list)