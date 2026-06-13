import io
import sys

_INPUT = """\
1112222334445556555

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
out = 0
now_same_count = 0
before_same_count = 0
before_num = -2
is_ok = False

for i, s in enumerate(list(S)):
    # 前の数字と同じならnow += 1
    if s == before_num:
        now_same_count += 1
    # 前の数字と違っている場合
    else:
        # is_okならbeforeとnowのminをoutに加算
        if is_ok:
            out += min(before_same_count, now_same_count)

        # nowをbeforeに,nowは1に
        before_same_count = now_same_count
        now_same_count = 1

        # 前の数字+1ならis_ok
        is_ok = int(s) == (int(before_num) + 1)

    before_num = s

if is_ok:
    out += min(before_same_count, now_same_count)


# 出力
print(out)
