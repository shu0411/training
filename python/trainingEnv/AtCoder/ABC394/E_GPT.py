import io
import sys

_INPUT = """\
4
ab--
--b-
---a
c---
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

from collections import deque

INF = 1000000010

def main():
    n = int(input())
    c = [input().strip() for _ in range(n)]
    a = [[INF] * n for _ in range(n)]
    que = deque()
    
    for i in range(n):
        que.append((i, i))
        a[i][i] = 0
    
    for i in range(n):
        for j in range(n):
            if i != j and c[i][j] != '-':
                que.append((i, j))
                a[i][j] = 1
    
    while que:
        i, j = que.popleft()
        for k in range(n):
            for l in range(n):
                if c[k][i] != '-' and c[j][l] != '-' and c[k][i] == c[j][l] and a[k][l] == INF:
                    a[k][l] = a[i][j] + 2
                    que.append((k, l))
    
    for i in range(n):
        print(' '.join(str(a[i][j]) if a[i][j] != INF else '-1' for j in range(n)))

if __name__ == "__main__":
    main()