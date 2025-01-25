import io
import sys

_INPUT = """\
3 5
.#?#.
.?#?.
?...?

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
H,W = map(int, input().split())
S = [input() for _ in range(H)]

#処理
min_L = 999
max_R = 0
min_U = 999
max_D = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            min_L = min(min_L, w)
            max_R = max(max_R, w)
            min_U = min(min_U, h)
            max_D = max(max_D, h)

for check_h in range(min_U, max_D+1):
    for check_w in range(min_L, max_R+1):
        if S[check_h][check_w] == ".":
            print("No")
            exit()

print("Yes")