import io
import sys

_INPUT = """\
http

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

S = input()

out = S + "s"
print(out)
