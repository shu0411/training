import io
import sys

_INPUT = """\
3
1 2 3
L??
"""
sys.stdin = io.StringIO(_INPUT)

#（問題）
#N
#P1 P2 ... PN   ←行動する順番
#S              ←人iが右利きか左利きか


#############ここから下をコピペ#############

#入力
N = int(input())
list_P = list(map(int, input().split()))
S = input()
list_spoon = [[1]*N]  #1=スプーンがある

#処理
out = 0

#i番目の人がスプーンを取れるか
def check(i):
    if list_spoon[i] == 1 and list_spoon[i+1] == 1:
        if S[i] == "L":
            list_spoon[i] = 0
        elif S[i] == "R":
            list_spoon[i+1] = 0
        
            


#出力
print(out)