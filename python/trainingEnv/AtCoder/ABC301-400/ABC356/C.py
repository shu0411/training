import io
import sys

_INPUT = """\
3 2 2
3 1 2 3 o
2 2 3 x
"""
sys.stdin = io.StringIO(_INPUT)

#N,M,K
#N→鍵の数
#M→テストの回数
#K→正しい鍵の数
#o→正しい鍵がすべて含まれている
#x→正しい鍵がすべて含まれていない

#3 2 2
#3 1 2 3 o
#2 2 3 x
#テスト結果1行目→1,2,3のうち2つが正しい鍵
#テスト結果2行目→少なくとも1は正しい鍵

#完了できず。本番後に修正。
#############ここから下をコピペ#############
import math
#入力
N,M,K = map(int,input().split())
table_CAR = [list(input().split()) for _ in range(M)]

#処理
list_o = [True] * N  #結果oから分かった正しい可能性のある鍵を格納
list_list_A_x = [] #結果がxだった時にテストした鍵のリスト

for list_CAR in table_CAR:
    C = int(list_CAR[0])
    list_A = list_CAR[1:C+1]
    R = list_CAR[-1]
    
    if R == "o":
        for i in range(N):
            if str(i+1) not in list_A:
                list_o[i] = False
    else:
        list_list_A_x.append(list_A)
        
print(list_o)

#list_oの中でTrueの数を数える
count_probably = 0
for i in range(N):
    if list_o[i]:
        count_probably += 1

set_x = set() #確実に正しい鍵のリスト
for list_A_x in list_list_A_x:
    if len(list_A_x) == count_probably - 1:
        for i in range(N):
            if str(i+1) not in list_A_x and list_o[i]:
                set_x.add(i+1)

count_correct = len(set_x)
count_left_probably = count_probably - count_correct

out = 0 #テスト結果を満たす正しい鍵の組み合わせ
left_correct = K - count_correct
if left_correct < 0 or left_correct > count_left_probably:
    out = 0
else:
    #count_probably個の鍵からleft_correct個の鍵を選ぶ
    out = math.factorial(count_left_probably) // (math.factorial(left_correct) * math.factorial(count_left_probably - left_correct))

#出力
print(out)