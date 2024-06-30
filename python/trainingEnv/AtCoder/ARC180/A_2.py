import io
import sys

_INPUT = """\
17
BBABABAABABAAAABA
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import queue

#入力
N = int(input())
S = input()

#処理
q1 = queue.LifoQueue()
set_S = set()

i = 0
q1.put([S,0])
set_S.add(S)

while not q1.empty():
    S,i = q1.get()
    if len(S) <= 2 or i >= len(S) - 2:
        continue
    if S[i:i+3] == "ABA":
        after_S = S[:i] + "A" + S[i+3:]
        q1.put([S,i+1])
        if after_S not in set_S:
            q1.put([after_S, i])
            set_S.add(after_S)
    elif S[i:i+3] == "BAB":
        after_S = S[:i] + "B" + S[i+3:]
        q1.put([S,i+1])
        if after_S not in set_S:
            q1.put([after_S, i])
            set_S.add(after_S)
    else:
        q1.put([S,i+1])

out = len(set_S)

#出力
print(out % (10**9 + 7))

#TLE