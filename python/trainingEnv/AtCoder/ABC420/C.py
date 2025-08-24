import io
import sys

_INPUT = """\
5 3
100 100 100 100 100
100 100 100 100 100
A 4 21
A 2 99
B 4 57

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

#処理
out = N

list_min_num = []
for i in range(N):
    min_num = min(list_A[i], list_B[i])
    list_min_num.append(min_num)

sum_min = sum(list_min_num)

for i in range(Q):
    #入力
    c,X,V = input().split()
    intX = int(X)
    intV = int(V)
    now_min = list_min_num[intX-1]
    if c == 'A':
        list_A[intX-1] = intV
    else:
        list_B[intX-1] = intV
    new_min = min(list_A[intX-1], list_B[intX-1])
    list_min_num[intX-1] = new_min
    sum_min += new_min - now_min

    print(sum_min)