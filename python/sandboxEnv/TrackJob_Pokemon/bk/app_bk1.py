#TLE。最初の回答。dict_kindなし
def create_solution(step: int, n: int, m: int, q: int, query1: list[int], query2: list[int], query3: list[int]) -> list[int]:
    # TODO: Implement this function
    dict_area = {}
    ans = []
    for i in range(q):
        if query3[i] != -1:
            #地域x{query1[i]}で種類y{query2[i]}のポケモンがz{query3[i]}匹発見された
            x = query1[i]
            y = query2[i]
            z = query3[i]
            if x not in dict_area:
                dict_area[x] = {}
            if y not in dict_area[x]:
                dict_area[x][y] = 0
            dict_area[x][y] += z
        else:
            #その地域で発見されているポケモンのうち、b{query2[i]}%以上が種類a{query1[i]}のポケモンである地域の数を出力する
            a = query1[i]
            b = query2[i]
            count = 0
            if b == 0:
                count = len(dict_area)
            else:
                for key, value in dict_area.items():
                    if a in value and value[a] / sum(value.values()) >= b / 100:
                        count += 1

            ans.append(count)

    return ans