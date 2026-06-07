import io
import sys

_INPUT = """\
2
3 4 5
40 20 30
10 100 50
1 2 3 4 5 6 7 8 9 10

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T = int(input())

#処理
for _ in range(T):
    N,K,X = map(int, input().split())
    list_A = list(map(float, input().split()))

    dic_len = {}
    for A in list_A:
        if A not in dic_len:
            dic_len[A] = 0
        dic_len[A] += 1
        
    dic_len_taple = sorted(dic_len.items(), key=lambda x: x[0], reverse=True)

    for _ in range(K):
        len,count = dic_len_taple.pop(0)
        if count >= 2:
            dic_len_taple.append((len, count - 1))
        dic_len_taple.append((len / 2, 2))
        dic_len_taple.sort(key=lambda x: x[0], reverse=True)
    
    while X > 0:
        length, count = dic_len_taple.pop(0)
        if count <= X:
            X -= count
            out = length

    #出力
    print(out)