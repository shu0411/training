import io
import sys

_INPUT = """\
6
71 74 45 34 31 60
"""
sys.stdin = io.StringIO(_INPUT)

#2 -> 0010
#5 -> 0101
#7 -> 0111
#XOR -> 0000

#2 5 7,0 7 7,0 5 9,2 0 12,0 0 14

#0 7 7
#0 -> 0000
#7 -> 0111
#7 -> 0111
#XOR -> 0000

#0 5 9
#0 -> 0000
#5 -> 0101
#9 -> 1001
#XOR -> 1100

#2 0 12
#2 -> 0010
#0 -> 0000
#12 -> 1100
#XOR -> 1110

#0 0 14
#0 -> 0000
#0 -> 0000
#14 -> 1110
#XOR -> 1110

#2 5 7
#2 5 7, 0 7 7, 0 5 9
#2 5 7, 0 7 7, 0 5 9, 2 0 12, 0 0 14
#############ここから下をコピペ#############

#入力
N = int(input())
list_A = list(map(int, input().split()))

#処理
set_tuple_after_A = set()   #作りうる配列を格納するset
set_tuple_after_A.add(tuple(list_A))
for i in range(N):
    tmp_set_tuple_after_A = set()
    for j in range(i+1,N):
        for tuple_after_A in set_tuple_after_A:
            list_after_A = list(tuple_after_A)
            list_after_A[j] = list_after_A[j] + list_after_A[i]
            list_after_A[i] = 0
            tmp_set_tuple_after_A.add(tuple(list_after_A))
    set_tuple_after_A = set_tuple_after_A.union(tmp_set_tuple_after_A)

set_xor = set()
for list_after_A in set_tuple_after_A:
    xor = 0
    for after_A in list_after_A:
        xor = xor ^ after_A
    set_xor.add(xor)

out = len(set_xor)

#出力
print(out)