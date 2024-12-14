import io
import sys

_INPUT = """\
128 256 512 1024 2048

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
list_score = list(map(int,input().split()))

#処理
list_record = []
for i in range(1,32):
    bit = format(i, '05b')
    name = ""
    tmp_name = "ABCDE"
    score = 0
    for j in range(5):
        if bit[j] == "1":
            name += tmp_name[j]
            score += list_score[j]
    list_record.append([name,score])

list_record.sort(key=lambda x: x[0])
list_record.sort(key=lambda x: x[1],reverse=True)

for record in list_record:
    print(record[0])