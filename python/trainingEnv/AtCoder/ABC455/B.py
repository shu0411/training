import io
import sys

_INPUT = """\
4 5
.#.#.
####.
##..#
....#

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
H, W = map(int, input().split())
table_S = [input() for _ in range(H)]

# 処理
out = 0

for h1 in range(H):
    for h2 in range(h1, H):
        for w1 in range(W):
            for w2 in range(w1, W):
                is_ok = True
                for i in range(h1, h2 + 1):
                    for j in range(w1, w2 + 1):
                        s1 = table_S[i][j]
                        s2 = table_S[h1 + h2 - i][w1 + w2 - j]
                        if s1 != s2:
                            is_ok = False
                            break
                    if not is_ok:
                        break

                if is_ok:
                    out += 1

# 出力
print(out)
