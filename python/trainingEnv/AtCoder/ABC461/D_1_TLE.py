import io
import sys

_INPUT = """\
15 20 17
10111101101100000100
01100000000010000011
01110010111000111000
11001100000111011000
10100001100011100010
01101000101010000101
10110001111110000100
10110011101100101101
01010001110011001001
01010110010001100110
01110100011110011110
01100000100111010010
11001101100111101100
10111100010101111011
00101101011100010000

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
H,W,K = map(int,input().split())
table_S = [input() for _ in range(H)]

#累積和
table_HW = [[0] * (W+1) for _ in range(H+1)]
for h in range(H):
    for w in range(W):
        table_HW[h+1][w+1] = table_HW[h][w+1] + table_HW[h+1][w] - table_HW[h][w] + int(table_S[h][w])

out = 0
# 処理
for uh in range(1,H+1):
    for dh in range(uh,H+1):
        for lw in range(1,W+1):
            for rw in range(lw,W+1):
                sum_hw = table_HW[dh][rw] - table_HW[uh-1][rw] - table_HW[dh][lw-1] + table_HW[uh-1][lw-1]
                if sum_hw == K:
                    out += 1
                elif sum_hw > K:
                    break

# 出力
print(out)
