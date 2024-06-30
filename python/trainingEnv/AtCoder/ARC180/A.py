import io
import sys

_INPUT = """\
4
ABAB
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
S = input()

#処理
set_S = set()
set_S.add(S)
before_S = ""
i = 0

while True:
    if len(S) <= 2:
        break

    if S[i:i+3] == "ABA":
        S = "A" + S[3:]
        set_S.add(S)
    
    elif S[i:i+3] == "BAB":
        S = "B" + S[3:]
        set_S.add(S)
    
    if S == before_S:
        i += 1
    
    if i >= len(S) - 2:
        break

    before_S = S

out = len(set_S)

#出力
print(out)