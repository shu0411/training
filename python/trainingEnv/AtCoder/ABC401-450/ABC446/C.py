import io
import sys

_INPUT = """\
3
3 1
7 2 3
1 3 2
3 2
7 2 3
1 3 2
2 1
2 1
1 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
from collections import deque

# 入力
T = int(input())

# 処理
for _ in range(T):
    N, D = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))
    out = N

    queue_egg = deque()
    sum_egg = 0

    for i in range(N):
        # 卵の追加
        add_egg = list_A[i]
        queue_egg.append((i, add_egg))  # 何日に何個の卵を入れたか
        sum_egg += add_egg

        # 卵の取り出し
        left_egg = list_B[i]
        sum_egg -= left_egg
        while left_egg > 0:
            j, got_egg = queue_egg.popleft()
            if left_egg < got_egg:
                queue_egg.appendleft((j, got_egg - left_egg))
                break
            left_egg -= got_egg

        # 期限切れの卵の廃棄
        if len(queue_egg) != 0:
            first_egg = queue_egg[0][0]

            if first_egg == i - D:
                _, drop_egg = queue_egg.popleft()
                sum_egg -= drop_egg

    # 出力
    print(sum_egg)
