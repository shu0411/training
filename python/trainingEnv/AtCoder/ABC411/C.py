import io
import sys

_INPUT = """\
3 3
1 3 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())
list_A = list(map(int, input().split()))

#処理
list_cell = [0] * (N + 2)
count_black = 0
for A in list_A:
    if list_cell[A] == 0:
        list_cell[A] = 1
        if list_cell[A - 1] == 0 and list_cell[A + 1] == 0:
            #両隣が白の場合、黒のエリアの数が1つ増える
            count_black += 1
        elif list_cell[A - 1] == 1 and list_cell[A + 1] == 1:
            #両隣が黒の場合、黒のエリアの数が1つ減る
            count_black -= 1
    elif list_cell[A] == 1:
        list_cell[A] = 0
        if list_cell[A - 1] == 0 and list_cell[A + 1] == 0:
            #両隣が白の場合、黒のエリアの数が1つ減る
            count_black -= 1
        elif list_cell[A - 1] == 1 and list_cell[A + 1] == 1:
            #両隣が黒の場合、黒のエリアの数が1つ増える
            count_black += 1

    #出力
    print(count_black)