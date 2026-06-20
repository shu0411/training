#TLE。dict_kindを作って、種類ごとにどの地域にいるか管理するように変更した。
def create_solution(step: int, n: int, m: int, q: int, query1: list[int], query2: list[int], query3: list[int]) -> list[int]:
    dict_area = {} #地域ごとに、その地域で発見されたポケモンの種類と数を記録
    dict_kind = {} #種類ごとに、そのポケモンがいる地域と数を記録
    ans = []
    for i in range(q):
        if query3[i] != -1:
            #地域x{query1[i]}で種類y{query2[i]}のポケモンがz{query3[i]}匹発見された
            x = query1[i]
            y = query2[i]
            z = query3[i]

            #dict_kindの更新
            if y not in dict_kind:
                dict_kind[y] = {}
            if x not in dict_kind[y]:
                dict_kind[y][x] = 0
            dict_kind[y][x] += z


            #dict_areaの更新
            if x not in dict_area:
                dict_area[x] = {}
            if y not in dict_area[x]:
                dict_area[x][y] = 0
            #dict_areaに地域xにいるポケモンの総数に対する種類yのを記録
            dict_area[x][y] += z
        else:
            #その地域で発見されているポケモンのうち、b{query2[i]}%以上が種類a{query1[i]}のポケモンである地域の数を出力する
            a = query1[i]
            b = query2[i]
            count = 0
            if b == 0:
                count = len(dict_area)
            elif a in dict_kind:
                for area in dict_kind[a]:
                    if dict_area[area][a] / sum(dict_area[area].values()) >= b / 100:
                        count += 1

            ans.append(count)

    return ans