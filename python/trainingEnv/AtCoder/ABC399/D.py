import io
import sys

_INPUT = """\
4
3
1 2 3 3 1 2
4
1 1 2 2 3 3 4 4
5
1 2 3 4 5 1 2 3 4 5
2
1 2 2 1
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T = int(input())    # テストケース数

#処理
for _ in range(T):
    #入力
    N = int(input())
    list_A = list(map(int,input().split()))

    #処理
    out = 0
    dic_A = {}
    for i in range(N * 2):
        if list_A[i] in dic_A:
            dic_A[list_A[i]].append(i)
        else:
            dic_A[list_A[i]] = [i]
    
    for A in dic_A:
        first_A = dic_A[A][0]
        second_A = dic_A[A][1]

        if first_A + 1 == second_A:
            continue

        if first_A > 0:
            prev_first_A = list_A[first_A - 1]
        else:
            prev_first_A = -1
        prev_second_A = list_A[second_A - 1]
        next_first_A = list_A[first_A + 1]
        if second_A < N * 2 - 1:
            next_second_A = list_A[second_A + 1]
        else:
            next_second_A = -2

        if (prev_first_A == prev_second_A and prev_first_A > A) \
            or (prev_first_A == next_second_A and prev_first_A > A) :
            out += 1
        if (next_first_A == prev_second_A and next_first_A > A and first_A + 2 != second_A and first_A + 3 != second_A) \
            or (next_first_A == next_second_A and next_first_A > A) :
            out += 1

    #出力
    print(out)