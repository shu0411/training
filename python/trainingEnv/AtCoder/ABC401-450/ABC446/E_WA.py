import io
import sys

_INPUT = """\
446 1 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
M, A, B = map(int, input().split())

# 処理
out = 0
for x in range(1, M):
    for y in range(1, M):
        s_n2 = x
        s_n1 = y
        first_mod_num = (A * s_n1 + B * s_n2) % M
        if first_mod_num == 0:
            continue
        s_n2 = s_n1
        s_n1 = first_mod_num
        while True:
            mod_num = (A * s_n1 + B * s_n2) % M
            if mod_num == first_mod_num:
                out += 1
                break
            if mod_num == 0:
                break

            s_n2 = s_n1
            s_n1 = mod_num

# 出力
print(out)
