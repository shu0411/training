import io
import sys

_INPUT = """\
5
6
SRRRSR
3 1 4 1 5 9
2 6 5 3 5
6
RSRSRS
10 10 10 10 10 10
1 1 1 1 1
2
RR
4 3
2
10
RSSRSSRSSR
75 49 79 37 16 9 38 49 69 54
23 100 73 63 66 23 51 65 67
20
SSSRSSSRRRRSSRSSRSSR
343191362 223147518 135066250 426658267 693515093 8023388 383375974 712283203 40447501 19870690 318452142 356265717 283999278 209219229 418603824 39363351 392058270 254796273 110117486 64951139
576697130 385986330 895027325 654885799 784214084 577658764 761714876 583039741 943991250 446493376 701505924 402891440 963636095 919408713 238125227 871191978 843843821 397910552 529447424

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
T = int(input())

for _ in range(T):
    N = int(input())
    S = input()
    list_X = list(map(int, input().split()))
    list_Y = list(map(int, input().split()))

    # 前の日が晴れ/雨だった時のMAX
    max_sunny = 0
    max_rainy = 0
    # 処理
    for i, s in enumerate(list(S)):
        if i == 0:
            if s == "S":
                max_sunny = 0
                max_rainy = -list_X[i]
            else:
                max_sunny = -list_X[i]
                max_rainy = 0
        else:
            tmp_max_sunny = max_sunny
            tmp_max_rainy = max_rainy
            if s == "S":
                max_sunny = max(tmp_max_sunny, tmp_max_rainy + list_Y[i - 1])
                max_rainy = max(tmp_max_sunny, tmp_max_rainy) - list_X[i]
            else:
                max_sunny = (
                    max(tmp_max_sunny, tmp_max_rainy + list_Y[i - 1]) - list_X[i]
                )
                max_rainy = max(tmp_max_sunny, tmp_max_rainy)

    out = max(max_sunny, max_rainy)

    # 出力
    print(out)
