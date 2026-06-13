import io
import sys

_INPUT = """\
20
67 296 399 8 10 351 227 392 212 104 265 390 394 39 165 129 183 200 167 357
82 33 197 264 194 393 329 177 218 283 293 379 74 173 149 258 166 207 241 117
225 72 364 220 53 178 185 279 163 384 326 239 308 48 179 184 280 64 103 99
140 66 344 158 26 27 11 223 142 291 51 196 141 295 16 110 317 313 309 391
345 12 25 14 45 328 373 224 233 146 385 18 339 352 282 358 118 249 181 294
367 360 145 288 250 368 195 214 231 323 100 30 322 332 311 205 213 208 336 235
340 269 395 32 92 246 321 234 398 238 186 278 273 276 41 52 3 302 245 202
86 83 136 244 107 54 383 128 7 90 89 355 84 55 380 160 341 98 270 348
175 69 159 228 346 60 331 135 327 365 189 215 21 108 24 263 303 28 382 222
132 19 305 255 361 80 35 112 152 68 209 324 236 388 369 192 363 237 76 154
6 286 62 338 156 277 187 13 111 347 65 232 71 268 198 204 377 366 20 257
290 171 119 378 310 259 306 137 298 397 335 61 320 70 96 5 162 371 58 49
330 349 147 144 370 274 304 97 148 1 191 131 318 101 153 334 78 133 57 127
88 174 0 77 356 297 376 221 123 289 151 267 59 281 44 285 271 29 253 91
134 114 260 217 342 23 261 315 46 176 143 40 113 362 210 120 180 292 150 396
75 130 240 262 115 284 182 353 374 319 287 381 247 81 256 17 164 386 63 121
155 350 38 36 94 170 139 337 389 307 106 116 343 31 85 252 95 230 272 22
251 229 211 188 242 300 50 243 325 226 4 168 190 219 169 301 375 79 124 266
161 201 372 105 359 333 126 42 314 248 387 138 312 37 15 87 122 157 275 109
316 216 56 125 34 199 102 299 254 193 43 47 93 206 354 73 2 172 9 203

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
table_a = [list(map(int, input().split())) for _ in range(N)]

# 変数定義

# 関数

def build_conveyors(N):
    conveyors = []

    # コンベア0: 外周を1周するループ（長さ 4*(N-1) = 76）
    # 経路: row0左→右, col(N-1)上→下, row(N-1)右→左, col0下→上
    # 出口(0, N//2)=(0,10) が含まれる
    conv0 = []
    for j in range(N):           # row0: 左→右
        conv0.append((0, j))
    for i in range(1, N):        # col(N-1): 上→下
        conv0.append((i, N - 1))
    for j in range(N - 2, -1, -1):  # row(N-1): 右→左
        conv0.append((N - 1, j))
    for i in range(N - 2, 0, -1):   # col0: 下→上
        conv0.append((i, 0))
    conveyors.append(conv0)

    # コンベア1〜9: 列ペア j,j+1 を行0〜N-1で1周する矩形ループ（長さ 2*N = 40）
    # 列1,2 / 3,4 / 5,6 / 7,8 / 9,10 / 11,12 / 13,14 / 15,16 / 17,18 の9本
    # 経路: (0,j)→(1,j)→...→(N-1,j)→(N-1,j+1)→(N-2,j+1)→...→(0,j+1) → (0,j)に戻る
    # row0 と row(N-1) で外周コンベアとマスを共有（受け渡しポイント）
    # col0 と col(N-1) は外周のみ（余計な重複を避ける）
    for k in range(N // 2 - 1):
        j = k * 2 + 1  # j = 1, 3, 5, ..., 17
        conv = []
        for i in range(N):               # col j: 上→下
            conv.append((i, j))
        for i in range(N - 1, -1, -1):  # col j+1: 下→上
            conv.append((i, j + 1))
        conveyors.append(conv)

    return conveyors


# 処理
conveyors = build_conveyors(N)

PERI_LEN = 4 * (N - 1)   # 外周の長さ = 76
EXIT_I, EXIT_J = 0, N // 2  # 出口座標 = (0, 10)
EXIT_PERI = EXIT_J          # 出口の外周インデックス = 10

# 状態: board[i][j]=箱番号(None=空), pos[k]=(i,j)
board = [row[:] for row in table_a]
pos = {table_a[i][j]: (i, j) for i in range(N) for j in range(N)}
next_to_ship = 0
ops = []

# 初期チェック: box0が出口にある場合は操作前に搬出
if board[EXIT_I][EXIT_J] == 0:
    board[EXIT_I][EXIT_J] = None
    del pos[0]
    next_to_ship = 1


def apply_op(m, d):
    global next_to_ship
    conv = conveyors[m]
    l = len(conv)
    ops.append((m, d))
    # 現在の内容を保存してシフト: 位置xの内容が位置(x+d)%lへ移動
    contents = [board[i][j] for (i, j) in conv]
    new_contents = [None] * l
    for x in range(l):
        new_contents[(x + d) % l] = contents[x]
    for x, (i, j) in enumerate(conv):
        board[i][j] = new_contents[x]
        if new_contents[x] is not None:
            pos[new_contents[x]] = (i, j)
    # 搬出判定: 出口に次に搬出すべき箱があれば除去
    box_at_exit = board[EXIT_I][EXIT_J]
    if box_at_exit is not None and box_at_exit == next_to_ship:
        board[EXIT_I][EXIT_J] = None
        del pos[next_to_ship]
        next_to_ship += 1


def perimeter_index(i, j):
    """外周コンベア内のインデックス(0〜PERI_LEN-1)を返す"""
    if i == 0:
        return j                      # row0: 0〜N-1
    elif j == N - 1:
        return (N - 1) + i            # 右辺: N〜2N-2
    elif i == N - 1:
        return 3 * (N - 1) - j        # row(N-1): 2N-1〜3N-3
    else:
        return 4 * (N - 1) - i        # 左辺: 3N-2〜4N-5


def find_vertical_conveyor(j):
    """j in [1..N-2] → (コンベア番号m, j_left, j_right)"""
    k = (j - 1) // 2
    j_left = 2 * k + 1
    j_right = j_left + 1
    return k + 1, j_left, j_right


# メインループ: box k を順番に搬出
for k in range(N * N):
    if k not in pos:
        continue  # すでに搬出済み
    i, j = pos[k]

    # ステップA: 縦コンベアでrow0へ移動（j=1〜18 かつ i>0 のとき）
    if 1 <= j <= N - 2 and i > 0:
        m, j_left, j_right = find_vertical_conveyor(j)
        if j == j_left:
            # (i, j_left) はコンベア内index=i → d=-1 で i 回動かすとindex=0=(0,j_left)
            for _ in range(i):
                apply_op(m, -1)
        else:
            # (i, j_right) はコンベア内index=2N-1-i → d=+1 で i 回動かすとindex=2N-1=(0,j_right)
            for _ in range(i):
                apply_op(m, 1)

    # ステップA中に搬出済み（j=10のj_rightケース）なら終了
    if k not in pos:
        continue

    # ステップB: 外周コンベアで出口へ移動
    i2, j2 = pos[k]
    peri_idx = perimeter_index(i2, j2)
    fwd = (EXIT_PERI - peri_idx) % PERI_LEN
    bwd = PERI_LEN - fwd

    if fwd == 0:
        # 既に出口にいる → conv1を1回動かして搬出チェックを発火
        apply_op(1, 1)
    elif fwd <= bwd:
        for _ in range(fwd):
            apply_op(0, 1)
    else:
        for _ in range(bwd):
            apply_op(0, -1)


# 出力
M = len(conveyors)
print(M)
for conv in conveyors:
    print(len(conv), " ".join(f"{i} {j}" for i, j in conv))

T = len(ops)
print(T)
for m, d in ops:
    print(m, d)
