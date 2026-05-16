import io
import sys

_INPUT = """\
1
4
2 3
4 5
6 7
8 9

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import heapq

# 入力
X = int(input())
Q = int(input())
lower_max_heapq = []
upper_min_heapq = []
center = X


# 関数
def add_lower(n):
    heapq.heappush(lower_max_heapq, -n)


def add_upper(n):
    heapq.heappush(upper_min_heapq, n)


def get_max_lower():
    return heapq.heappop(lower_max_heapq) * (-1)


def get_min_upper():
    return heapq.heappop(upper_min_heapq)


# クエリ
for i in range(Q):
    A, B = map(int, input().split())
    if A > center and B > center:
        add_upper(A)
        add_upper(B)
        add_lower(center)
        center = get_min_upper()
    elif A >= center and B <= center:
        add_upper(A)
        add_lower(B)
    elif A <= center and B >= center:
        add_lower(A)
        add_upper(B)
    elif A < center and B < center:
        add_lower(A)
        add_lower(B)
        add_upper(center)
        center = get_max_lower()

    # 出力
    print(center)
