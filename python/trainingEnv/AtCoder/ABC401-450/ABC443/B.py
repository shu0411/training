import io
import sys

_INPUT = """\
4 43

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

N, K = map(int, input().split())

age = N
count = 0
while count < K:
    count += age
    age += 1

print(age - 1 - N)
