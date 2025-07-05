import io
import sys

_INPUT = """\
3 4 7
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
a,b,C = map(int,input().split())

#処理
#Cをビット化
C_bit = format(C, 'b')
len_C_bit = len(C_bit)




#出力
print(C_bit)