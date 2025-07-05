import io
import sys

_INPUT = """\
osangelesa
LAX
"""
sys.stdin = io.StringIO(_INPUT)
#以下のいずれかの条件を満たすかどうかを判定する。
#S の長さ 3 の（連続とは限らない）部分列をとり、それを英大文字に変換したものを T とする
#S の長さ 2 の（連続とは限らない）部分列をとり、それを英大文字に変換したものの末尾に X を追加したものを T とする
#############ここから下をコピペ#############

#入力
S = input()
T = input()

#処理
out = "Yes"

#Sを大文字に変換
S = S.upper()

#Tの3文字目がXの場合
if T[2] == "X":
    #Tの1文字目のSの中での出現箇所
    index1 = S.find(T[0])
    #Tの2文字目のSの中での出現箇所
    index2 = S.find(T[1], index1 + 1)
    #Tの1文字目と2文字目がSに含まれているかどうか
    if index1 == -1 or index2 == -1:
        out = "No"
    
#Tの3文字目がX以外の場合
else:
    #Tの1文字目のSの中での出現箇所
    index1 = S.find(T[0])
    #Tの2文字目のSの中での出現箇所
    index2 = S.find(T[1], index1 + 1)
    #Tの3文字目のSの中での出現箇所
    index3 = S.find(T[2], index2 + 1)
    #Tの1文字目と2文字目がSに含まれているかどうか
    if index1 == -1 or index2 == -1 or index3 == -1:
        out = "No"

#出力
print(out)