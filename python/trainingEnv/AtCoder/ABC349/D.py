import io
import sys

_INPUT = """\
5 7
"""
sys.stdin = io.StringIO(_INPUT)

'''
2**aがlを超える最小のa
2**bがrを超えない最大のb
これをつなぐ。
l→a→b→r'''
#############ここから下をコピペ#############

#入力
l,r = map(int,input().split())

#処理
a=0
b=0
#l以上で最小の2**i=a
if l == 0:
    a=0
else:
    for i in range(60):
        if 2**i >= l:
            a=2**i
            break
#rを超えない最大の2**b
for i in range(60):
    if 2**i > r:
        b=2**(i-1)
        break


#l→a→b→r
#a-l,b-a,r-bをビット化
bit_la = bin(a - l)[2:]
bit_ab = bin(b - a)[2:]
bit_rb = bin(r - b)[2:]

#3つのビットの1の数を数える
count = bit_la.count('1') + bit_ab.count('1') + bit_rb.count('1')

#出力
if a <= b:
    print(count)

    #ビットの逆順にbeforeに2**iを足していく
    before = l
    i = 0
    for x in bit_la[::-1]:
        if x == '1':
            after = before + 2**i
            print(str(before) + " " + str(after))
            before = after
        i += 1

    i = 0
    for x in bit_ab[::-1]:
        if x == '1':
            after = before + 2**i
            print(str(before) + " " + str(after))
            before = after
        i += 1

    i = len(bit_rb) - 1
    for x in bit_rb:
        if x == '1':
            after = before + 2**i
            print(str(before) + " " + str(after))
            before = after
        i -= 1
else:
    bit_lr = bin(r - l)[2:]
    count = bit_lr.count('1')

    print(count)
    before = l
    i = 0
    for x in bit_lr[::-1]:
        if x == '1':
            after = before + 2**i
            print(str(before) + " " + str(after))
            before = after
        i += 1
#WAあり