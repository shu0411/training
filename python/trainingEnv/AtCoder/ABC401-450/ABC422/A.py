import io
import sys

_INPUT = """\
7-8

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
world,stage = S.split("-")
stage = int(stage) + 1
if stage == 9:
    world = int(world) + 1
    stage = 1
out = str(world) + "-" + str(stage)

#出力
print(out)