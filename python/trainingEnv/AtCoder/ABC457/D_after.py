import io
import sys

_INPUT = """\
20 457
8 9 10 9 8 8 4 6 8 1 5 10 2 8 2 6 8 1 6 6

"""
sys.stdin = io.StringIO(_INPUT)

# Kに対する解は単調増加→解の二分探索が有効
# 解をX以上にすることができる最小回数はK回以下か？

#############ここから下をコピペ#############

# 入力
N, K = map(int, input().split())
list_A = list(map(int, input().split()))


# 関数
def is_ok(x: int):
    """K回で解をx以上にできるか"""
    count_times = 0
    for i, A in enumerate(list_A):
        if A < x:
            count_times += (x - A - 1) // (i + 1) + 1
            if count_times > K:
                return False
    return True


# 処理:解の二分探索
ans_min = 1
ans_max = list_A[0] + K + 1  # 上限は必ずFalseになる必要あり
while ans_max - ans_min > 1:
    check_x = (ans_max + ans_min) // 2
    if is_ok(check_x):
        ans_min = check_x
    else:
        ans_max = check_x

# 出力
print(ans_min)
