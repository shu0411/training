import io
import sys

_INPUT = """\
wwwwwwwwwv

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
dic = {}
for s in S:
    if s not in dic:
        dic[s] = 0
    dic[s] += 1

out = ""
for key,value in dic.items():
    if value == 1:
        out = key

#出力
print(out)