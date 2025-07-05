import io
import sys

_INPUT = """\
0 0 0 1000 1000 1000
10 10 10 100 100 100
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
a,b,c,d,e,f = map(int,input().split())
g,h,i,j,k,l = map(int,input().split())

#処理
out = "Yes"

if j<=a or d<=g:
    out = "No"
elif k<=b or e<=h:
    out = "No"
elif l<=c or f<=i:
    out = "No"

#出力
print(out)