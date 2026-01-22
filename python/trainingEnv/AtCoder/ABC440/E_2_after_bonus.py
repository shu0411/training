import io
import sys

_INPUT = """\
9 14142 13
31 41 59 26 53 58 97 93 23

"""
sys.stdin = io.StringIO(_INPUT)

# 増やすべきは、
# 個数が0でないもののうち、一番Aが小さいもの(以後 min_idx ）にかかわる操作だけ。
# ・min_idx の個数を1つ減らして min_idx+1 の個数を1つ増やしたもの（ min_idx が最後の要素(N-1)じゃない場合）
# ・min_idx-1 の個数を1つ減らして、min_idx の個数を1つ増やしたもの（min_idx-1 の個数が0じゃない場合）
# ※この操作の逆が1回しか起こらない＝この操作でできる組み合わせも重複しない
#
# 妥協操作を「末尾の非0要素に関するもの」に正規化している。
# 任意の配分はこの規則に従う一意な親を必ず持つため、
# 状態全体が木構造になり、重複なく全パターンを網羅できる。

#############ここから下をコピペ#############
import heapq

# 入力
N, K, X = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
list_out = []

list_A.sort(reverse=True)
list_queue_pair = [(list_A[0] * K * (-1), int(0), int(0), K)]
heapq.heapify(list_queue_pair)

i = 0
while i < X:
    popped = heapq.heappop(list_queue_pair)
    popped_sum = popped[0]
    popped_min_idx = popped[1]
    popped_before_min_count = popped[2]
    popped_min_count = popped[3]
    i += 1

    # 出力
    print(popped_sum * (-1))

    # 次の追加処理
    if popped_min_idx != N - 1:
        heapq.heappush(
            list_queue_pair,
            (
                popped_sum + list_A[popped_min_idx] - list_A[popped_min_idx + 1],
                popped_min_idx + 1,
                popped_min_count - 1,
                1,
            ),
        )

    if popped_before_min_count != 0:
        heapq.heappush(
            list_queue_pair,
            (
                popped_sum + list_A[popped_min_idx - 1] - list_A[popped_min_idx],
                popped_min_idx,
                popped_before_min_count - 1,
                popped_min_count + 1,
            ),
        )
