import io
import sys

_INPUT = """\
100 132 10 10000
75 98
7 63
2 63
20 77
26 91
52 74
35 50
12 34
19 32
60 75
31 69
28 97
37 48
79 86
37 41
51 63
44 67
11 38
88 97
2 73
22 27
61 81
71 94
12 64
36 61
1 96
17 38
36 66
4 81
4 72
12 25
56 70
40 56
1 65
14 19
73 94
69 95
46 93
22 72
33 35
3 17
89 91
41 69
0 29
45 49
9 63
77 82
46 59
38 88
52 73
30 99
28 36
43 90
15 33
6 75
16 59
23 47
78 95
86 92
23 94
22 32
21 57
40 42
6 53
23 84
1 99
48 70
7 16
72 96
21 72
3 84
29 49
9 39
24 43
45 85
49 68
10 72
24 90
58 61
21 96
39 71
21 22
31 41
25 55
6 98
47 74
3 74
10 58
5 8
80 90
62 72
26 83
24 34
14 60
20 56
17 74
15 83
30 34
48 54
11 20
13 40
27 87
87 91
64 99
17 54
0 18
67 93
54 78
92 99
44 88
13 76
65 89
53 77
6 20
0 85
33 76
33 50
65 96
14 97
51 80
5 59
54 68
35 82
42 82
18 71
57 89
4 36
8 73
62 99
55 79
47 52
66 93
7 130
295 259
71 36
75 149
232 155
98 44
170 222
86 17
125 70
12 30
252 151
112 202
256 34
57 274
166 159
290 296
130 18
87 167
37 104
186 162
144 241
261 211
222 205
45 123
193 76
232 28
248 280
211 247
173 133
4 154
272 97
16 245
208 179
214 297
238 75
151 295
200 122
56 253
116 148
48 34
98 273
31 275
108 295
224 48
128 131
11 0
155 66
91 100
75 229
1 179
182 281
150 7
124 91
200 225
62 195
182 27
101 220
246 229
260 115
126 41
161 185
228 108
284 140
47 1
281 55
266 243
209 101
149 98
21 166
5 287
80 257
21 49
276 180
84 77
101 134
159 205
59 295
166 256
44 207
185 1
165 43
239 135
129 268
271 269
34 150
8 101
256 2
202 278
141 159
248 253
186 50
219 267
281 28
169 97
68 90
1 202
286 216
152 135
194 198
297 117

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import queue

# 入力
N, M, K, T = map(int, input().split())
dict_edge = {i: [] for i in range(N)}
for i in range(M):
    A, B = map(int, input().split())
    dict_edge[A].append(B)
    dict_edge[B].append(A)

# 処理
list_out = []
steps = 0
visited_1 = [True] + [False] * (N - 1)
list_route = [0]
q1 = queue.Queue()
q1.put([steps, visited_1, list_route])
is_reached_shop = False
# 最短で到達できるショップ
while not is_reached_shop and steps <= T:
    if q1.empty():
        break
    steps, visited_1, list_route = q1.get()
    steps += 1
    now_node = list_route[-1]
    for next_node in dict_edge[now_node]:
        tmp_visited_1 = visited_1.copy()
        tmp_list_route = list_route.copy()
        if tmp_visited_1[next_node]:
            continue
        tmp_list_route.append(next_node)
        tmp_visited_1[next_node] = True
        # 次の点がショップだったら終了
        if next_node < K:
            list_route = tmp_list_route
            is_reached_shop = True
            break

        q1.put([steps, tmp_visited_1, tmp_list_route])

q2 = queue.Queue()
base_shop_node = list_route[-1]
before_node = list_route[-2]
list_loop_route = [base_shop_node]
visited_2 = [True] + [False] * (N - 1)
is_finished_loop = False
q2.put([steps, visited_2, list_loop_route])
while not is_finished_loop and steps <= T:
    if q2.empty():
        break
    steps, visited_2, list_loop_route = q2.get()
    steps += 1
    now_node = list_loop_route[-1]
    for next_node in dict_edge[now_node]:
        tmp_visited_2 = visited_2.copy()
        tmp_list_loop_route = list_loop_route.copy()
        if len(tmp_list_loop_route) >= 2:
            before_node = tmp_list_loop_route[-2]

        if next_node == before_node:
            continue

        # スタートのショップに戻ってきたらそれをループとみなして終了。
        if next_node == base_shop_node:
            list_loop_route = tmp_list_loop_route
            is_finished_loop = True
            break

        if tmp_visited_2[next_node]:
            continue

        tmp_list_loop_route.append(next_node)
        tmp_visited_2[next_node] = True

        # 次の点がショップだったらその経路を捨てて続行
        if next_node < K:
            continue

        q2.put([steps, tmp_visited_2, tmp_list_loop_route])

# 出力
last_steps = 0
for node in list_route[1:]:
    last_steps += 1
    if last_steps >= T:
        break
    print(node)

for node in list_loop_route[1:]:
    last_steps += 1
    if last_steps >= T:
        break
    print(node)

if last_steps < T:
    last_steps += 1
    print(base_shop_node)

for i in range(len(list_loop_route)):
    if last_steps >= T:
        break
    steps_in_loop_count = 0
    for node in list_loop_route[1:]:
        if i == steps_in_loop_count:
            print(-1)
            last_steps += 1
        print(node)
        steps_in_loop_count += 1
        last_steps += 1

    print(base_shop_node)
    last_steps += 1
