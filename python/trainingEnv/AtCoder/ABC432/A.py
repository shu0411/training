import io
import sys

_INPUT = """\
9 1 9

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
list_ABC = input().split()

# 処理
list_ABC.sort(reverse=True)

# 出力
print(list_ABC[0] + list_ABC[1] + list_ABC[2])
