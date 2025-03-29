import io
import sys

_INPUT = """\
<><><
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import queue

#入力
S = input()

#処理
out = "Yes"
queue = queue.LifoQueue()
for s in S:
    if s == "(" or s == "[" or s == "<":
        queue.put(s)
    elif s == ")":
        if queue.empty() or queue.get() != "(":
            out = "No"
            break
    elif s == "]":
        if queue.empty() or queue.get() != "[":
            out = "No"
            break
    elif s == ">":
        if queue.empty() or queue.get() != "<":
            out = "No"
            break

if not queue.empty():
    out = "No"

#出力
print(out)