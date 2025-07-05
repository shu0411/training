import io
import sys

_INPUT = """\
5
3 4 1 2 5
"""
sys.stdin = io.StringIO(_INPUT)
#コンテスト中のソース。WA
#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int,input().split()))

#処理
list_A = [0] + list_A
count = 0
list_change = []

for i in range(1,N+1):
    #list_Aにiが出てくる順番を取得
    if list_A[i] != i:
        tmp = list_A[i]
        count += 1
        if i < tmp:
            list_change.append([i,tmp])
        else:
            list_change.append([tmp,i])
        #i番目とtmp番目を入れ替える
        list_A[i],list_A[tmp] = list_A[tmp],list_A[i]

#出力
print(count)
#list_changeを空白区切りで出力
for i in range(count):
    print(list_change[i][0],list_change[i][1])

#WAあり