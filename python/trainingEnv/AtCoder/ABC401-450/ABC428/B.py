import io
import sys

_INPUT = """\
35 3
thequickbrownfoxjumpsoverthelazydog

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, K = map(int, input().split())
S = input()

# 処理
dic_s = {}
for i in range(N - K + 1):
    tmp_str = S[i : i + K]
    if tmp_str not in dic_s:
        dic_s[tmp_str] = 0
    dic_s[tmp_str] += 1

max_val = max(dic_s.values())
max_key = [kv[0] for kv in dic_s.items() if kv[1] == max_val]
max_key.sort()

# 出力
print(max_val)
print(*max_key)
