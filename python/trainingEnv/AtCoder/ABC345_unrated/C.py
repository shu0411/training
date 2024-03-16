import io
import sys

_INPUT = """\
aaaaab
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
available_pattern = len(S) * (len(S) - 1) / 2  #入れ替え可能なすべてのパターン
same_pattern = 0    #同じ文字を入れ替えるパターン

#アルファベットの個数を取得
alphabet_Dic = {}
for i in range(97,97+26):
    alphabet_Dic[chr(i)] = 0

for s in S:
    alphabet_Dic[s] += 1

for k in alphabet_Dic.keys():
    #アルファベットごとの個数
    cnt = alphabet_Dic[k]
    #同じ文字を入れ替えるパターンの数
    if cnt >= 2:
        same_pattern += cnt * (cnt-1) / 2

#元と同じパターンが１つでもあったら、それも1パターンとして数えられるので-1
if same_pattern != 0:
    same_pattern -= 1

out = int(available_pattern) - int(same_pattern)

#出力
print(out)