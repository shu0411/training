import io
import sys

_INPUT = """\
123456789012345
"""
sys.stdin = io.StringIO(_INPUT)

#その数字が立方数かどうかを判定する方法は、誤差が出るためあきらめた。
#誤差を許容する方法は後で考える。
#############ここから下をコピペ#############

#入力
N = int(input())

#処理
#小さいほうから順に立方回文数を求める（10の18条までに15個）
i = 0
out = 0
list_n = []
while True:
    i += 1
    number = i ** 3
    if number > N:
        #numberがNを超えた時点で、その前のnumberを出力して終了
        print(out)
        break
    if number == int(str(number)[::-1]):
        out = number
