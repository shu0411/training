import io
import sys

_INPUT = """\
bananabbxx
"""
sys.stdin = io.StringIO(_INPUT)
#良い文字列：S にちょうど i 回現れる文字はちょうど 0 種類またはちょうど 2 種類ある
#S が良い文字列かどうか判定してください。
#Sの中の文字ごとの出現回数を数える
#############ここから下をコピペ#############

#入力
S = input()

#処理
#Sの中の文字ごとの出現回数を数える
dic = {}
for s in S:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

#出現回数ごとのdictを作成
dic2 = {}
for key in dic:
    if dic[key] in dic2:
        dic2[dic[key]] += 1
    else:
        dic2[dic[key]] = 1

#dic2のvalueが0または2でないものがあるかどうか
out = "Yes"
for key in dic2:
    if dic2[key] != 0 and dic2[key] != 2:
        out = "No"
        break

#出力
print(out)