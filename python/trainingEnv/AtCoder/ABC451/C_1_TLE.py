import io
import sys

_INPUT = """\
12
2 256601193
1 85138616
1 202564041
2 276477192
1 55551662
1 170271057
2 754166580
1 854388209
1 772036624
2 651124113
1 301137866
2 290875185

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
Q = int(input())

# 処理
total_cnt = 0
dict_h_cnt = {}
for _ in range(Q):
    kind, h = map(int, input().split())

    if kind == 1:
        if h not in dict_h_cnt:
            dict_h_cnt[h] = 0
        dict_h_cnt[h] += 1
        total_cnt += 1
    else:
        list_keys = list(dict_h_cnt.keys())
        list_keys.sort()
        for key_dict_h in list_keys:
            if key_dict_h <= h:
                del_cnt = dict_h_cnt.pop(key_dict_h)
                total_cnt -= del_cnt
            else:
                break

    # 出力
    print(total_cnt)
