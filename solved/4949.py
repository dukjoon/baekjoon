while 1:
    x = str(input())
    if x == '.':
        break
    a_1 = x.count('(')
    a_2 = x.count(')')
    b_1 = x.count('[')
    b_2 = x.count(']')
    c_1 = x.count('{')
    c_2 = x.count('}')
    if a_1 == a_2 and b_1 == b_2 and c_1 == c_2:
        print("yes")
    else:
        print("no")