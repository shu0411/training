import io
import sys

_INPUT = """\
5 3
13 13 13 13 2
5
12
13

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())
list_A = list(map(int, input().split()))

#処理
list_A.sort()
max_A = max(list_A)
len_A = len(list_A)

dic_count_A = {}
for A in list_A:
    if A in dic_count_A:
        dic_count_A[A] += 1
    else:
        dic_count_A[A] = 1

list_ans = [0]
b = 0
sum_less = 0
count_less = 0
for i in dic_count_A:
    while b < i:
        tmp = sum_less + (len_A - count_less) * b + 1
        list_ans.append(tmp)
        b += 1
    sum_less += dic_count_A[i] * i
    count_less += dic_count_A[i]

for i in range(Q):
    #入力
    x = int(input())

    #処理
    out = 0
    if x > max_A:
        out = -1
    else:
        out = list_ans[x]

    #出力
    print(out)