import io
import sys

_INPUT = """\
2 6
2 1 at
3 1
2 2 on
1 2
2 2 coder
3 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())

server = ""
dict_pc = {}
for _ in range(Q):
    #処理
    query = input().split()
    if query[0] == "1":
        #PCpをサーバーで置き換え
        p = int(query[1])
        if p not in dict_pc:
            dict_pc[p] = ""
        dict_pc[p] = server
    elif query[0] == "2":
        #PCpの末尾に文字列を追加
        p = int(query[1])
        s = query[2]
        if p not in dict_pc:
            dict_pc[p] = ""
        dict_pc[p] += s
    elif query[0] == "3":
        #サーバーをPCpで置き換え
        p = int(query[1])
        if p in dict_pc:
            server = dict_pc[p]
        else:
            server = ""

#出力
print(server)