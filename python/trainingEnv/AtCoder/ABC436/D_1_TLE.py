import io
import sys

_INPUT = """\
7 11
u..#y..#...
k..#.z.#.k.
iju#...#x..
###########
..x#.t.#..n
abc#y..#...
..z#..t#.y.

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import queue

# 入力
H, W = map(int, input().split())
table_S = []
dic_warp = {}
for i in range(H):
    tmp_S = input()
    table_S.append(tmp_S)
    for j, s in enumerate(list(tmp_S)):
        if s not in ["#", "."]:
            if s not in dic_warp:
                dic_warp[s] = []
            dic_warp[s].append((i, j))

# 処理
out = -1

visited = [[-1] * W for _ in range(H)]
list_tuple_dir = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

queue_next = queue.Queue()
queue_next.put((0, 0))
visited[0][0] = 0
while not queue_next.empty():
    now_pos = queue_next.get()
    now_count = visited[now_pos[0]][now_pos[1]]
    if now_pos[0] == H - 1 and now_pos[1] == W - 1:
        out = now_count
        break

    # ワープ処理
    now_s = table_S[now_pos[0]][now_pos[1]]
    if now_s not in ["#", "."]:
        for check_pos_warp in dic_warp[now_s]:
            if visited[check_pos_warp[0]][check_pos_warp[1]] != -1:
                continue

            visited[check_pos_warp[0]][check_pos_warp[1]] = now_count + 1
            queue_next.put(check_pos_warp)

    # 移動処理
    for tuple_dir in list_tuple_dir:
        check_pos_h = now_pos[0] + tuple_dir[0]
        check_pos_w = now_pos[1] + tuple_dir[1]

        if check_pos_h < 0 or check_pos_h >= H or check_pos_w < 0 or check_pos_w >= W:
            continue

        if visited[check_pos_h][check_pos_w] != -1:
            continue

        if table_S[check_pos_h][check_pos_w] == "#":
            continue

        visited[check_pos_h][check_pos_w] = now_count + 1
        queue_next.put((check_pos_h, check_pos_w))

# 出力
print(out)
