import io
import sys

_INPUT = """\
2
20 2
1234567890 17
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T = int(input())

#処理
for i in range(T):
    #入力
    N, K = map(int, input().split())

    #出力
    bin_N = bin(N)[2:] #Nを2進数に変換
    len_N = len(bin_N) #Nの2進数桁数


    bin(N).count("1")
    out = 0 #出力用変数
    

    #出力
    print(out)