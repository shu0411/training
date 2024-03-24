import io
import sys

_INPUT = """\
3 3 2
)))(()
"""
sys.stdin = io.StringIO(_INPUT)
#（問題）
#N A B
#S

#正しい括弧列とは，以下のいずれかの条件を満たす文字列です．
#・空文字列
#・ある正しい括弧列 A が存在して，(, A, ) をこの順に結合した文字列
#・ある空でない正しい括弧列 S,T が存在して，S,T をこの順に結合した文字列
#↓
#・(と)の数が一致している。
#・左から見て、常に(の数が)の数以上である
#・右端が)である
#↓
#()の数を一致させる。
#その後左からチェック。(の数が)の数以上であるか
#############ここから下をコピペ#############

#入力
N,A,B = map(int, input().split())
S = input()

#処理
#()の数を合わせる
left = 0
right = 0
for i in range(len(S)):
    if S[i] == "(":
        left += 1
    else:
        right += 1

if left > right:
    for i in range(left - right):
        #右端から"("を")"に変える
        S = S[::-1].replace("(",")",1)[::-1]
elif right > left:
    for i in range(right - left):
        #左端から")"を"("に変える
        S = S.replace(")","(",1)

#左からチェック
change_times = 0
check = 0
for i in range(len(S)):
    if S[i] == "(":
        check += 1
    else:
        check -= 1
    if check < 0:
        #)が大きい場合、一番右にある(と交換する
        change_times += 1
        check = 0

out = A * change_times + B * abs(left - right)

#出力
print(out)