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

#動的計画法を勉強する。
#https://atcoder.jp/contests/abc344/submissions/51029984
#############ここから下をコピペ#############
