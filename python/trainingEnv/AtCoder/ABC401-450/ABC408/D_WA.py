import io
import sys

_INPUT = """\
1
23
01010100111001110101010
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T = int(input())

#処理
for _ in range(T):
    N = int(input())
    S = "0" + input()
    
    list_area = []
    list_len = []
    tmp_begin = 0
    for i,s in enumerate(S):
        if s == "1" and tmp_begin == 0:
            tmp_begin = i  
        elif s == "0" and tmp_begin != 0:
            list_area.append([tmp_begin, i])
            list_len.append(i - tmp_begin)
            tmp_begin = 0
    if tmp_begin != 0:
        list_area.append([tmp_begin, N + 1])
        list_len.append(N + 1 - tmp_begin)

    if len(list_area) <= 1:
        print(0)
        continue

    max_len_id = list_len.index(max(list_len))

    out = 0
    for i in range(max_len_id):
        len_area = list_area[i][1] - list_area[i][0]
        if i < len(list_area) - 1:
            len_next = list_area[i + 1][0] - list_area[i][1]
    
        out += min(len_area, len_next)
    for i in range(max_len_id + 1, len(list_area)):
        len_area = list_area[i][1] - list_area[i][0]
        if i > 0:
            len_before = list_area[i][0] - list_area[i - 1][1]
        else:
            len_before = 0
        
        out += min(len_area, len_before)
    
    #出力
    print(out)