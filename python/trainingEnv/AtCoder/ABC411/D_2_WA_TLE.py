import io
import sys

_INPUT = """\
10 10
2 7 ladxf
2 7 zz
2 7 kfm
3 7
1 5
2 5 irur
3 5
1 6
2 6 ptilun
3 6


"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())

server = []
dict_pc = {}
list_str = []
str_id = 0
for _ in range(Q):
    #処理
    query = input().split()
    if query[0] == "1":
        #PCpをサーバーで置き換え
        p = int(query[1])
        if p not in dict_pc:
            dict_pc[p] = []
        dict_pc[p] = server.copy()
        
    elif query[0] == "2":
        #PCpの末尾に文字列を追加
        p = int(query[1])
        s = query[2]
        list_str.append(s)

        if p not in dict_pc:
            dict_pc[p] = []
        dict_pc[p].append(str_id)

        str_id += 1

    elif query[0] == "3":
        #サーバーをPCpで置き換え
        p = int(query[1])
        if p in dict_pc:
            server = dict_pc[p].copy()
        else:
            server = []

#出力
out_str = ""
for i in server:
    out_str += list_str[i]

print(out_str)