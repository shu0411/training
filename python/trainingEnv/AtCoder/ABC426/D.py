import io
import sys

_INPUT = """\
3
5
01001
3
000
15
110010111100101

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T = int(input())

#処理
for _ in range(T):
    N = input()
    S = input()
    
    max_count = [0,0]
    count_all = [0,0]
    before = ""
    count = 0
    for s in S:
        count_all[int(s)] += 1
        if s != before:
            if before != "":
                max_count[int(before)] = max(max_count[int(before)],count)
            before = s
            count = 1
        else:
            count += 1
    else:
        max_count[int(S[-1])] = max(max_count[int(S[-1])],count)
    
    move_count_0 = count_all[1] + (count_all[0] - max_count[0]) * 2
    move_count_1 = count_all[0] + (count_all[1] - max_count[1]) * 2
    
    out = min(move_count_0,move_count_1)
    
    #出力
    print(out)