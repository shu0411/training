import io
import sys

_INPUT = """\
3
5 1 1 1 1 1
4 2 2 2 2
3 1 1 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())

#処理
list_dict_prob = []

#入力と、それぞれのサイコロの各目の出る確率を辞書型で保存
for i in range(N):
    #入力
    K, *list_A = map(int, input().split())
    list_A.sort()

    #それぞれのサイコロの各目の出る確率
    dict_count = {}
    for a in list_A:
        if a in dict_count:
            dict_count[a] += 1
        else:
            dict_count[a] = 1

    dict_prob = {}
    for key,count in dict_count.items():
        dict_prob[key] = count/K
    
    list_dict_prob.append(dict_prob)

#2つのサイコロの組み合わせを全て調べ、出る目が同じ確率を計算
list_prob = []
for i in range(N):
    for j in range(i+1, N):
        tmp_prob = 0
        dict_prob_i = list_dict_prob[i]
        dict_prob_j = list_dict_prob[j]
        for key,prob_i in dict_prob_i.items():
            if key in dict_prob_j:
                tmp_prob += prob_i * dict_prob_j[key]
    
        list_prob.append(tmp_prob)

max_prob = 0
if len(list_prob) > 0:
    max_prob = max(list_prob)

#出力
print(max_prob)