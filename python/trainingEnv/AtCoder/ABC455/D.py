import io
import sys

_INPUT = """\
5 4
3 1
4 5
3 2
5 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import sys

sys.setrecursionlimit(3 * 10**5)

# 入力
N, Q = map(int, input().split())
dic_connection = {i: -1 for i in range(1, N + 1)}
dic_count = {i: 0 for i in range(1, N + 1)}
dic_visited_last_key = {i: -1 for i in range(1, N + 1)}


# def
def count_up(now_key, now_count):

    if dic_visited_last_key[now_key] != -1:
        visited_last_key = dic_visited_last_key[now_key]
        dic_count[visited_last_key] += now_count
        return visited_last_key

    now_count += 1

    next_key = dic_connection[now_key]

    if next_key == -1:
        dic_visited_last_key[now_key] = now_key
        dic_count[now_key] = now_count
        return now_key

    last_key = count_up(next_key, now_count)
    dic_visited_last_key[now_key] = last_key
    return last_key


# 処理
for _ in range(Q):
    C, P = map(int, input().split())
    dic_connection[C] = P

for key in dic_connection.keys():
    count_up(key, 0)

# 出力
list_out = list(dic_count.values())
print(*list_out)
