import io
import sys

_INPUT = """\
2 1 4 2
"""
sys.stdin = io.StringIO(_INPUT)
#入力：左下(A,B)、右上(C,D)の座標
# パターン：
# (0,0)～(4,2)の範囲のパターンは
# 1 2 1 0
# 2 1 0 1
# →ここの合計は8
# これが繰り返されているだけ。
# ここからはみ出している部分を考慮していく
# 

#############ここから下をコピペ#############

# (0,0)～(4,2)の範囲のパターンは
# 1 2 1 0
# 2 1 0 1
#この4*2の範囲のパターンが繰り返されている。
#入力
A, B, C, D = map(int, input().split())

#処理
out = 0

#パターン部分 ★ここの計算にNGあり。修正必要
#x座標のパターン部分
x = int(C/4) - int(A/4)
#y座標のパターン部分
y = int(D/2) - int(B/2)
out += 8 * x * y

#はみ出している部分
if A % 4 == 0:
    left = 0
else:
    left = 4 - A % 4
right = C % 4
top = D % 2
if B % 2 == 0:
    bottom = 0
else:
    bottom = 2 - B % 2

#左のはみだしの計算
if left >= 1:
    out += 1 * y + 1 * top + 0 * bottom
if left >= 2:
    out += 1 * y + 0 * top + 1 * bottom
if left >= 3:
    out += 3 * y + 1 * top + 2 * bottom

#右のはみだしの計算
if right >= 1:
    out += 3 * y + 2 * top + 1 * bottom
if right >= 2:
    out += 3 * y + 1 * top + 2 * bottom
if right >= 3:
    out += 1 * y + 0 * top + 1 * bottom

#上のはみだしの計算
if top == 1:
    out += 4 * x

#下のはみだしの計算
if bottom == 1:
    out += 4 * x    

#出力
print(out)
#WA