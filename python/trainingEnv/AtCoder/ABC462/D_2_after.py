import io
import sys

_INPUT = """\
4 1
1 1000000
1 1000000
1 1000000
1 1000000

"""
sys.stdin = io.StringIO(_INPUT)

# <反省>
# 人ごとに数えようとしてしまった→(N + 1) * N / 2 回計算が必要→計算量が多くなる。
# 時間を固定する方法がないか？→「その時刻が犯行開始時刻だった場合に」という仮定。
# あとは知っているimos法を使うだけ。
#############ここから下をコピペ#############

# 入力
N, D = map(int, input().split())

# 処理
max_time = 10**6 + 1
list_imos_count = [0] * max_time  # その時刻が犯行開始時刻だった場合に
for i in range(N):
    S, T = map(int, input().split())
    if T - S >= D:
        list_imos_count[S] += 1
        list_imos_count[T - D + 1] -= 1

out = 0
tmp_count = 0
for i in range(max_time):
    tmp_count += list_imos_count[i]
    if tmp_count >= 2:
        out += tmp_count * (tmp_count - 1) // 2

# 出力
print(out)
