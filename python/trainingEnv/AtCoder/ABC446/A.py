import io
import sys

_INPUT = """\
Fred


"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
out = "Of" + S.lower()

# 出力
print(out)
