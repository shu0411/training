import io
import sys

_INPUT = """\
10 2
1011111111

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,K = map(int,input().split())
S = input()

#処理
one_group_count = 0 #1のグループの個数
change_count = 0    #変更する個数
before_pos = 0      #移動前の位置
after_pos = 0       #移動後の位置

before = "0"    #前の文字
change_flg = False  #変更フラグ(1のグループがK個になったか)
target_flg = False  #対象フラグ(K-1個目の1の位置を見つけたか)
for i,s in enumerate(S):
    if s == "1":
        if before == "0":
            one_group_count += 1
            if one_group_count == K - 1:
                target_flg = True
            if one_group_count == K:
                before_pos = i
                change_flg = True
        if change_flg:
            change_count += 1
    elif target_flg:
        after_pos = i
        target_flg = False
    elif change_flg:
        break

    before = s

out = S[:after_pos] + ("1" * change_count) + ("0" * (before_pos - after_pos)) + S[(before_pos+change_count):]

#出力
print(out)