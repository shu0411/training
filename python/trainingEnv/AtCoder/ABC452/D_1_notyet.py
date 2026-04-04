import io
import sys

_INPUT = """\
abrakadabra
aba

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()
T = input()

# 処理
dict_s = {chr(i): [] for i in range(97, 97 + 26)}
for i, s in enumerate(list(S)):
    dict_s[s].append(i)


# 出力
print(dict_s)
