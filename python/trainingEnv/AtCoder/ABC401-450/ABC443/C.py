import io
import sys

_INPUT = """\
10 1234
395 424 588 745 773 863 910 958 1102 1195

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, T = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
count_full = 0
last_sec = 0
before_sec = -100
for A in list_A:
    if A < before_sec + 100:
        continue

    # 就業時間より100秒以内なら終了
    if A >= T - 100:
        last_sec = T - A
        break

    count_full += 1
    before_sec = A

out = T - (count_full * 100 + last_sec)

# 出力
print(out)
