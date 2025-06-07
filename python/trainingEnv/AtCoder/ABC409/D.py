import io
import sys

_INPUT = """\
3
7
atcoder
1
x
5
snuke

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T = int(input())

#処理
for _ in range(T):
    N = int(input())
    S = input()
    for i in range(N-1):
        if S[i] > S[i+1]:
            for j in range(i+1, N):
                if S[i] < S[j]:
                    S = S[:i] + S[i+1:j] + S[i] + S[j:]
                    break
            else:
                S = S[:i] + S[i+1:] + S[i]
            break

    #出力
    print(S)