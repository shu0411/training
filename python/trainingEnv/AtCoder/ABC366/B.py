import io
import sys

_INPUT = """\
4
atcoderxx
beginnerxxxxd
contest
aaaaaaaaaaaa
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_S = [input() for i in range(N)]

#処理
max_len = 0
max_len_list = [] #そこまでの最大長を保存しておく
for i in range(N):
    max_len = max(max_len,len(list_S[i]))
    max_len_list.append(max_len)

for i in range(max_len):
    out = ""
    for j in range(N-1,-1,-1):
        if len(list_S[j]) > i:
            out += list_S[j][i]
        elif max_len_list[j] > i:
            out += "*"

    #出力
    print(out)