import io
import sys

_INPUT = """\
4 5 3
3 1 2 3 o
3 2 3 4 o
3 3 4 1 o
3 4 1 2 o
4 1 2 3 4 x
"""
sys.stdin = io.StringIO(_INPUT)

#N,M,K
#N→鍵の数
#M→テストの回数
#K→必要最低限の正しい鍵の数
#o→正しい鍵がK本以上含まれている
#x→正しい鍵がK本未満

#本番後に修正したもの。AC
#############ここから下をコピペ#############
#入力
N,M,K = map(int,input().split())
table_CAR = [list(input().split()) for _ in range(M)]

#処理
#bit全探索
out = 0
for i in range(2**N):
    bit_i = format(i, '0'+str(N)+'b')

    #1=正しい鍵, 0=正しくない鍵とみなして、テスト結果と矛盾しないか確認
    result = True
    for list_CAR in table_CAR:
        C = int(list_CAR[0])
        list_A = list_CAR[1:C+1]
        R = list_CAR[-1]
        
        count_correct = 0
        for j in range(N):
            if bit_i[j] == "1" and str(j+1) in list_A:
                count_correct += 1
        if count_correct >= K and R == "x":
            result = False
            break
        if count_correct < K and R == "o":
            result = False
            break
    
    if result:
        out += 1

#出力
print(out)