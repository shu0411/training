import io
import sys

_INPUT = """\
9 14142 13
31 41 59 26 53 58 97 93 23

"""
sys.stdin = io.StringIO(_INPUT)

# heapqは昇順の方が管理しやすいため、合計の個数だけはマイナスで管理
# 愚直に1か所を1減らし次を1増やした組み合わせを加えていく
# 配列は前のものをコピーし、対象idxを-1,idx+1を+1する
# setでこれまでにキューに入れた組み合わせを管理
#############ここから下をコピペ#############
import heapq

# 入力
N, K, X = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
list_out = []

list_A.sort(reverse=True)

first_pair = (list_A[0] * K * (-1), tuple([K] + [0] * (N - 1)))
list_queue_pair = [first_pair]
set_seen_pair = set()
heapq.heapify(list_queue_pair)
i = 0
while i < X:
    popped = heapq.heappop(list_queue_pair)
    popped_sum = popped[0]
    popped_pair = popped[1]
    i += 1

    # 出力
    print(popped_sum * (-1))

    # 次の追加処理
    for idx, num in enumerate(popped_pair):
        if num == 0 or idx >= N - 1:
            continue

        list_next = list(popped_pair)
        list_next[idx] -= 1
        list_next[idx + 1] += 1

        tuple_next = tuple(list_next)
        if tuple_next in set_seen_pair:
            continue

        set_seen_pair.add(tuple_next)

        heapq.heappush(
            list_queue_pair,
            (
                popped_sum + list_A[idx] - list_A[idx + 1],
                tuple_next,
            ),
        )
