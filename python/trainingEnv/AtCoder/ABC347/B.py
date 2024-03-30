import io
import sys

_INPUT = """\
abracadabra
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
set_s = set()
#全ての部分文字列をset_sに入れる
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        set_s.add(S[i:j])

#出力
print(len(set_s))