import io
import sys

_INPUT = """\
17
AAABABABBBABABBABABABABBAAABABABBA

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
S = input()

#処理
out = 0

#A始まり
count_A = 0
count_move_A = 0
for i in range(len(S)):
    if S[i] == "A":
        move = abs(i - (count_A * 2 + 1))
        count_move_A += move
        count_A += 1
    

#B始まり
count_B = 0
count_move_B = 0
for i in range(len(S)):
    if S[i] == "B":
        move = abs(i - (count_B * 2 + 1))
        count_move_B += move
        count_B += 1

out = min(count_move_A, count_move_B)

#出力
print(out)