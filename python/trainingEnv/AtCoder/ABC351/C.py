import io
import sys

_INPUT = """\
8
2 1 1 3 5 3 3 4
"""
sys.stdin = io.StringIO(_INPUT)
#N回ループ
#i番目とlist_Bの末尾が異なる場合、list_Bにlist_A[i]を追加
#i番目とlist_Bの末尾が同じ場合、list_Bの末尾を+1した上で、以下の操作を実施
#list_Bの末尾から順に戻っていき、jとj-1番目の要素が同じ場合、j-1番目を+1してjを削除
#j番目とj-1番目が異なったらループ終了。つぎのi番目へ
#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))

#処理
list_B = []
for i in range(N):
    if i == 0:
        list_B.append(list_A[i])
        continue
    if list_A[i] != list_B[-1]:
        list_B.append(list_A[i])
    else:
        list_B[-1] += 1
        for j in range(len(list_B)-1, 0, -1):
            if list_B[j] == list_B[j-1]:
                list_B[j-1] += 1
                list_B.pop(j)
            else:
                break

out = len(list_B)

#出力
print(out)