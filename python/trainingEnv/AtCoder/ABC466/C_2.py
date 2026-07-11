# 入力
N = int(input())

# 処理
pair_count = 0
r = 2

for l in range(1, N):
    if l == r:
        r += 1

    # 出力
    print("?", l, r)

    # 入力
    tmp_input = input()

    # 処理
    while tmp_input == "Yes":

        if r < N:
            r += 1
            # 出力
            print("?", l, r)

            # 入力
            tmp_input = input()
        else:
            pair_count += r - l
            break
    else:
        pair_count += r - l - 1


# 最終出力
print("!", pair_count, flush=True)
