import io
import sys

_INPUT = """\
3 4 3
1001
1101
0110

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
        table_HW[h+1][w+1] = table_HW[h][w+1] + int(table_S[h][w])

out = 0
# 処理
for uh in range(1,H+1):
    for dh in range(uh,H+1):
        lw = 1
        rw = 1
        for lw in range(1,W+1):
            sum_hw = 0
            while rw < W and sum_hw < K:
                sum_hw += table_HW[dh][rw] - table_HW[uh-1][rw]
                rw += 1
                if sum_hw == K:
                    out += 1
        
            if lw == rw:
                rw += 1
            else:
                sum_hw -= table_HW[dh][lw] - table_HW[uh-1][lw]

# 出力
print(out)
