import io
import sys

_INPUT = """\
10
2
1
3
1
3
1
1
3
2
2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
Q = int(input())

# 処理
volume = 0
is_playing = False
for _ in range(Q):
    A = input()
    if A == "1":
        volume += 1
    elif A == "2":
        volume = max(volume - 1, 0)
    else:
        is_playing = not is_playing

    out = "No"
    if is_playing and volume >= 3:
        out = "Yes"

    # 出力
    print(out)
