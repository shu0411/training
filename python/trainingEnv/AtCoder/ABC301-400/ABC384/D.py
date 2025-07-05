import io
import sys

_INPUT = """\
20 85415869
748 169 586 329 972 529 432 519 408 587 138 249 656 114 632 299 984 755 404 772

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,S = map(int,input().split())
list_A = list(map(int,input().split()))

#処理
out = "No"
sum_A = sum(list_A)
tmp_S = S % sum_A

if tmp_S == 0:
    out = "Yes"

list_A_double = list_A + list_A
left = 0
right = 0
tmp_sum = 0
while right < 2*N:
    tmp_sum += list_A_double[right]
    right += 1
    if tmp_sum > tmp_S:
        while tmp_sum > tmp_S and left <= right:
            tmp_sum -= list_A_double[left]
            left += 1
    if tmp_sum == tmp_S:
        out = "Yes"
        break


#出力
print(out)