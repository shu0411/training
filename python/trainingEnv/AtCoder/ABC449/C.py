import io
import sys

_INPUT = """\
10 2 6
aabbccaabb

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, L, R = map(int, input().split())
S = "_" + input()

# 処理
dict_char_cnt = {chr(i): [0] * (N + 1) for i in range(97, 123)}

for i in range(1, N + 1):
    for chr_key in dict_char_cnt.keys():
        if S[i] == chr_key:
            dict_char_cnt[chr_key][i] = dict_char_cnt[chr_key][i - 1] + 1
        else:
            dict_char_cnt[chr_key][i] = dict_char_cnt[chr_key][i - 1]

out = 0
for i in range(1, N + 1):
    s = S[i]
    cnt_range_R = min(i + R, N)
    cnt_range_L = min(i + L - 1, N)
    tmp = dict_char_cnt[s][cnt_range_R] - dict_char_cnt[s][cnt_range_L]
    out += tmp

# 出力
print(out)
