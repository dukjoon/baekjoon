def han(num):
    han_count = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            han_count += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            han_count += 1
    return han_count

num = int(input())
print(han(num))