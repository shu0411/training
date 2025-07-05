import io
import sys

_INPUT = """\
4
cat
enate
on
c

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_S = []

#処理
for _ in range(N):
    tmp_s = input()
    list_S.append((tmp_s, len(tmp_s)))
list_S.sort(key=lambda x: x[1])

out = ""
for s,_ in list_S:
    out += s

#出力
print(out)