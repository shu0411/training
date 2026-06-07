import io
import sys

_INPUT = """\
Serval Ocelot

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
X,Y = input().split()

#処理
list_os = ["Ocelot", "Serval", "Lynx" ]


X_idx = list_os.index(X)
Y_idx = list_os.index(Y)

out = "No"

if X_idx >= Y_idx:
    out = "Yes"

#出力
print(out)