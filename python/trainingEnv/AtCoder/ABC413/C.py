import io
import sys

_INPUT = """\
10
1 160449218 954291757
2 17217760
1 353195922 501899080
1 350034067 910748511
1 824284691 470338674
2 180999835
1 131381221 677959980
1 346948152 208032501
1 893229302 506147731
2 298309896

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
Q = int(input())

#処理
list_now_cnt = []
list_now_num = []
next_list_index = 0
next_inner_index = 0

for i in range(Q):
    #入力
    list_query = list(map(int, input().split()))

    #処理
    if list_query[0] == 1:
        list_now_cnt.append(list_query[1])
        list_now_num.append(list_query[2])
    
    elif list_query[0] == 2:
        plus_cnt = list_query[1]

        #カウントを進める処理
        now_sum = 0
        left_plus_cnt = plus_cnt
        while left_plus_cnt > 0:
            next_cnt_item = list_now_cnt[next_list_index]
            if left_plus_cnt >= next_cnt_item - next_inner_index:
                now_sum += list_now_num[next_list_index] * (next_cnt_item - next_inner_index)
                left_plus_cnt -= next_cnt_item - next_inner_index
                next_list_index += 1
                next_inner_index = 0
            else:
                now_sum += list_now_num[next_list_index] * left_plus_cnt
                next_inner_index += left_plus_cnt
                left_plus_cnt = 0
        
        print(now_sum)