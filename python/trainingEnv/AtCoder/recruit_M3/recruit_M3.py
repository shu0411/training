import io
import sys

_INPUT = """\
"Scala is a general purpose programming language designed to express common programming patterns in a concise, elegant, and type-safe way. It smoothly integrates features of object-oriented and functional languages, enabling Java and other programmers to be more productive. Code sizes are typically reduced by a factor of two to three when compared to an equivalent application by Java."
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

def solution(text):
    # TODO: Implement me!
    list_S = text.split()

    set_S = set()
    for s in list_S:
        tmp = s.replace('"', '').replace('.', '').replace(',', '')
        if tmp[0].isupper() or tmp[0].isdigit():
            set_S.add(tmp)
    
    return len(set_S)


#入力
S = input()

#処理
out = solution(S)

#出力
print(out)