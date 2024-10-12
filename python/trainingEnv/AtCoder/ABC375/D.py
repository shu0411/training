import io
import sys

_INPUT = """\
XYYXYYXYXXX
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
out = 0
len_S = len(S)
dic_s = {}
dic_len = {}
dic_sum = {}
for i in range(len_S):
    if S[i] in dic_s:
        #S[i]が既に登録されている場合
        tmp_out = dic_sum[S[i]] + (dic_len[S[i]] * (i - dic_s[S[i]][-1])) - 1
        dic_len[S[i]] += 1
        dic_sum[S[i]] = tmp_out
        dic_s[S[i]].append(i)
        out += tmp_out
    else:
        dic_s[S[i]] = [i]
        dic_len[S[i]] = 1
        dic_sum[S[i]] = 0

print(out)