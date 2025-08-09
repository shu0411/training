import io
import sys

_INPUT = """\
ottottott

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
list_count_t = [0]
count_t = 0
for i in range(len(S)):
    if S[i] == "t":
        count_t += 1
    list_count_t.append(count_t)

max_ratio = 0
for i in range(len(S)+1):
    for j in range(i + 3, len(S)+1):
        count_t = list_count_t[j] - list_count_t[i]
        ratio = (count_t - 2) / (j - i - 2)
        if max_ratio < ratio:
            max_ratio = ratio

#出力
print(max_ratio)