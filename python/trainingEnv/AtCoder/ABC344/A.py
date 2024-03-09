import io
import sys

_INPUT = """\
atcoder|beginner|contest
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
firstBar = S.find('|')
lastBar = S.rfind('|')
out = S[:firstBar] + S[lastBar+1:]

#出力
print(out)