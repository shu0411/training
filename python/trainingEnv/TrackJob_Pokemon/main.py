import sys
from app import create_solution

#############ここから下は不要#############

import io

_INPUT = """\
1
2
3
5
5
1
1
1
2
3
5
1
2
50
50
0
5
6
4
-1
-1
-1
"""
sys.stdin = io.StringIO(_INPUT)
#入力内容
# step
# n
# m
# q
# n_query1
# query1（要素数n_query1のリスト）
# n_query2
# query2（要素数n_query2のリスト）
# n_query3
# query3（要素数n_query3のリスト）

#クエリ内容（2種類）
#※query1, query2, query3は引数を表す。
#q回の処理でquery1, query2, query3の要素を順に使う
#1種類目（≠query1）
#query3の値が-1以外の場合はこっち
#x = query1[i], y = query2[i], z = query3[i]
#地域xで種類yのポケモンがをz匹発見された
#2種類目（≠query2）
#query3の値が-1の場合はこっち
#a = query1[i], b = query2[i]
#その地域で発見されているポケモンのうち、b%以上が種類aのポケモンである地域の数を出力する

#出力内容
#地域の数
#※要素数は、2種類目のクエリの数と同じ
#############ここから下をコピペ#############


def read_inputs() -> tuple[int, int, int, int, list[int], list[int], list[int]]:
    step = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    q = int(sys.stdin.readline())
    n_query1 = int(sys.stdin.readline())
    query1 = []
    for _ in range(n_query1):
        query1.append(int(sys.stdin.readline()))
    n_query2 = int(sys.stdin.readline())
    query2 = []
    for _ in range(n_query2):
        query2.append(int(sys.stdin.readline()))
    n_query3 = int(sys.stdin.readline())
    query3 = []
    for _ in range(n_query3):
        query3.append(int(sys.stdin.readline()))
    return step, n, m, q, query1, query2, query3,


def print_result(xs: list[int]):
    print(len(xs))
    for x in xs:
        print(x)


step, n, m, q, query1, query2, query3, = read_inputs()
result = create_solution(step, n, m, q, query1, query2, query3)
print_result(result)
