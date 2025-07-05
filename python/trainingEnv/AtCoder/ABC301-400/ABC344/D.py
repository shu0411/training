import io
import sys

_INPUT = """\
abcde
3
3 ab abc abcd
4 f c cd bcde
2 e de
"""
sys.stdin = io.StringIO(_INPUT)

#まずは愚直に全探索してみる
#→TLEになる
#時間切れ

#############ここから下をコピペ#############

#入力
T = input()
N = int(input())
table_S = []

#処理
out = 101
#各list_Sから1つまたは0つ選んで、Tになるかを探す
list_tmp_S = [["",0]]

for i in range(N):
    list_S = input().split()[1:]
    
    tmp_list_tmp_S = []
    for tmp_S in list_tmp_S:
        if tmp_S[0] == T:
            break
        for s in list_S:
            if tmp_S[0] + s == T[:len(tmp_S[0] + s)]:
                tmp_list_tmp_S.append([tmp_S[0] + s, tmp_S[1]+1])
    list_tmp_S = list_tmp_S + tmp_list_tmp_S

for tmp_S in list_tmp_S:
    if tmp_S[0] == T:
        if tmp_S[1] < out:
            out = tmp_S[1]

if out == 101:
    out = -1

#出力
print(out)