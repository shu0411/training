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

list_query = []
for _ in range(Q):
    #処理
    query = input().split()
    list_query.append(query)

now_server = "0"
now_str_rev = ""
#クエリをさかのぼって文字列のリストを生成
for query in list_query[::-1]:
    if query[0] == "1":
        #PCpをサーバーで置き換え
        if now_server == query[1]:
            now_server = "0"
    elif query[0] == "2":
        #PCpの末尾に文字列を追加
        if now_server == query[1]:
            now_str_rev += query[2][::-1]
        
    elif query[0] == "3":
        #サーバーをPCpで置き換え
        if now_server == "0":
            now_server = query[1]

#出力
out_str = now_str_rev[::-1]

print(out_str)