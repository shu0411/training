import io
import sys

_INPUT = """\
10 99
"""
sys.stdin = io.StringIO(_INPUT)

# メモ
#ヘビ数の条件
#1番上の位が1→下の位は0のみ
#1番上の位が2→下の位は1,0のみ
#1番上の位がN→下の位はN-1以下

#同じ桁数のヘビ数の合計
#3桁→１＋４＋９＋１６＋２５＋３６＋４９＋６４＋８１＝285
#4桁→１＋８＋２７＋６４＋１２５＋２１６＋３７５＋５７６＋８１９＝2209
#############ここから下をコピペ#############

#関数
#その桁以下のヘビ数の個数を返す再帰関数
#i:上からの桁数
#firstN:最上位の数字
#strN:元の数字
def count_snake_sub(i, strN):
    ret = 0
    nowN = int(strN[i])
    lenN = len(strN)
    firstN = int(strN[0])

    if i == lenN-1:
        #最後の桁の場合
        return min(nowN + 1, firstN)
    else:
        #最後の桁以外の場合
        if nowN >= firstN:
            #最上位の数字以上の場合
            ret += firstN ** (lenN-i)
        else:
            #最上位の数字より小さい場合
            ret += nowN * (firstN ** (lenN-i-1))
            ret += count_snake_sub(i+1, strN)
        return ret

def count_snake(n):
    ret = 0
    strN = str(n)
    lenN = len(strN)
    firstN = int(strN[0])
    secondN = int(strN[1])

    #1からRまでのヘビ数の個数
    #1つ前の桁まで
    for i in range(2,lenN):
        for j in range(1,10):
            ret += j**(i-1)

    #最後の桁(1つ前の数字まで)
    for i in range(1,firstN):
        ret += i**(lenN-1)

    #最後の桁(最後の数字)
    ret += count_snake_sub(1, strN)
        
    return ret
            
#入力
L,R = map(int,input().split())

#処理
outL = count_snake(L-1) if L > 10 else 0
outR = count_snake(R)

#出力
print(outR - outL)