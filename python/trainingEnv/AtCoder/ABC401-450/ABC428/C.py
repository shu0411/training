import io
import sys

_INPUT = """\
8
1 (
2
1 (
1 )
2
1 (
1 )
1 )

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

from collections import deque

# 入力
Q = int(input())

# 処理
stack_s = deque()
stack_pair = deque()
stack_unpair_left = deque()
stack_unpair_right = deque()
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        c = query[1]
        len_s = len(stack_s)
        stack_s.append(c)
        if c == "(":
            stack_unpair_left.append(len_s)
        else:
            if len(stack_unpair_left) == 0:
                stack_unpair_right.append(len_s)
            elif (
                len(stack_unpair_right) == 0
                or stack_unpair_left[-1] >= stack_unpair_right[-1]
            ):
                left = stack_unpair_left.pop()
                stack_pair.append((left, len_s))
            else:
                stack_unpair_right.append(len_s)
    else:
        pop_c = stack_s.pop()
        len_s = len(stack_s)
        if pop_c == "(":
            stack_unpair_left.pop()
        else:
            if len(stack_unpair_right) != 0 and stack_unpair_right[-1] == len_s:
                stack_unpair_right.pop()
            else:
                left, right = stack_pair.pop()
                stack_unpair_left.append(left)

    if len(stack_unpair_left) == 0 and len(stack_unpair_right) == 0:
        out = "Yes"
    else:
        out = "No"

    # 出力
    print(out)
