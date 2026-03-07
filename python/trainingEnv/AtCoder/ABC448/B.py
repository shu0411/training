import io
import sys

_INPUT = """\
15 10
7 94 100 82 63 81 75 2 76 73
10 44
5 77
10 47
7 32
2 82
5 90
3 37
6 70
6 28
3 25
2 26
10 56
1 69
5 46
7 26

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
list_C = list(map(int, input().split()))

dict_pepper = {i: [] for i in range(1, M + 1)}
for _ in range(N):
    A, B = map(int, input().split())
    dict_pepper[A].append(B)

# 処理
sum_gram = 0
for idx, list_gram in dict_pepper.items():
    list_gram.sort(reverse=True)
    left_pepper = list_C[idx - 1]
    for gram in list_gram:
        if gram < left_pepper:
            sum_gram += gram
            left_pepper -= gram
        else:
            sum_gram += left_pepper
            break


# 出力
print(sum_gram)
