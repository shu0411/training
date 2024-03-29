import io
import sys

_INPUT = """\
11
11111100111
512298012 821282085 543342199 868532399 690830957 973970164 928915367 954764623 923012648 540375785 925723427
"""
sys.stdin = io.StringIO(_INPUT)

#(問題)
#N
#S
#C1 C2 ... CN
#良い文字列＝ i文字目とi+1文字目が一致するようなものがちょうど1つだけ存在する
#良い文字列の例）10010
#悪い文字列の例）11011、00011
#iごとにi番目の0と1を入れ替える。ただし、Ciのコストがかかる
#最小のコストで良い文字列にする

#(方針)
#基本的には交互、1か所だけ連続する。
#1の連続する部分を見つけ、その部分を交互に変えていく
#例：00011で良い文字列にするiの組み合わせは
#1と5   →10010
#2      →01011
#3と4   →00101

#長さNの文字列Tを仮定したとき、いい文字列の組み合わせは、
#0始まりのとき連続する可能性のある個所がN-1か所
#1始まりのとき連続する可能性のある個所がN-1か所
#→最大で2(N-1)か所。Nが最大で2*10^5なので、全探索できる
#TとSの差分をとり、その差分のCを合計

#例）N=5のとき、できる良い文字列は
#00101,01101,01001,01011,11010,10010,10110,10100
#それぞれ、00011との差分は
#00101→3,4      →2+6=8
#01101→2,3,4    →9+2+6=17
#01001→2,4      →9+6=15
#01011→2        →9
#11010→1,2,5    →3+9+4=16
#10010→1,5      →3+4=7
#10110→1,3,5    →3+2+4=9
#10100→1,3,4,5  →3+2+6+4=15
#最小のコストは7

#(方針変更)
#0始まりの01交互文字列と、1始まりの10交互文字列を作成
#それとはじめからi番目、i番目から最後までのコストを計算しておく
#jを1からN-1まで動かし、j番目にj-1番目と同じ文字を挿入するていで、0はじまり、1はじまりのコストを両方計算

#############ここから下をコピペ#############

#入力
N = int(input())
S = input()
list_C = list(map(int, input().split()))

#処理
out = 10**14 * 2
#0始まりで0と1が交互になる長さN-1の文字列を作成
tmp_T="01" * ((N-1)//2) + "0"*((N-1)%2)
#2番目からN番目までに１つ前と同じ文字を挿入(i=1～N-1)して文字列Tを作成
for j in range(1, N):
    #文字列Tを作成
    T = tmp_T[:j] + tmp_T[j-1] + tmp_T[j:]

    #TとSの差分をとり、その差分のCを合計
    cost = 0
    for i in range(N):
        if T[i] != S[i]:
            cost += list_C[i]
    out = min(out, cost)

#1始まりで0と1が交互になる長さN-1の文字列Tを作成
tmp_T="10" * ((N-1)//2) + "1"*((N-1)%2)
#2番目からN番目までに１つ前と同じ文字を挿入
for j in range(1, N):
    #文字列Tを作成
    T = tmp_T[:j] + tmp_T[j-1] + tmp_T[j:]

    #TとSの差分をとり、その差分のCを合計
    cost = 0
    for i in range(N):
        if T[i] != S[i]:
            cost += list_C[i]
    out = min(out, cost)

#出力
print(out)