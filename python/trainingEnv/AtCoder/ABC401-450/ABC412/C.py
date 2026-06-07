import io
import sys

_INPUT = """\
1
10
11 3 2 5 4 6 7 8 9 10
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T = int(input())

#処理
for i in range(T):
    N = int(input())
    list_S = list(map(int, input().split()))
    
    S_1 = list_S[0]
    S_N = list_S[-1]
    sorted_list_S = sorted(list_S[1:-1])

    out = 2
    now = S_1
    before = -1
    now_index = 0
    if S_N > now * 2:
        while now_index < len(sorted_list_S):
            S = sorted_list_S[now_index]
            if now <= S <= now * 2:
                before = S
                now_index += 1
            elif now * 2 < S and before != -1:
                out += 1
                now = before
                if S_N <= now * 2:
                    break
            else:
                now_index += 1
        else:
            if out != -1:
                if now < before <= now * 2:
                    now = before
                    if S_N <= now * 2:
                        out += 1
                    else:
                        out = -1
                elif before == -1 and now * 2 < S_N:
                    out = -1

    #出力
    print(out)