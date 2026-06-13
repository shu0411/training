import io
import sys

_INPUT = """\
5
3
0010000
3
0111100
1
1
2
110
4
001110010101110

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#関数：深さ優先探索
def dfs( n, n_bit, S, seen ):
    seen[n] = True

    #nが2**N-1になればOK
    if seen[2**len(n_bit) - 1]:
        return

    for i in range(len(n_bit)):
        if n_bit[(i+1)*(-1)] == '0':
            new_n = n + (1 << i)

            #新しいn番目が1のときはスキップ
            if S[new_n-1] == '1':
                continue
                
            if not seen[new_n]:
                new_n_bit = bin(new_n)[2:].zfill(len(n_bit))
                dfs(new_n, new_n_bit, S, seen)
            

#入力
T = int(input())

#処理
for _ in range(T):
    N = int(input())
    S = input()
    
    seen = [False] * (2 ** N)
    first_n_bit = "0" * N

    dfs(0, first_n_bit, S, seen)

    out = "No"
    if seen[2**N - 1]:
        out = "Yes"

    #出力
    print(out)