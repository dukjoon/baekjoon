# asdf = 'asdf'
a = input().upper()
b = list(set(a))

cnt_list = []
for x in b :
    cnt = a.count(x)
    cnt_list.append(cnt)
      
if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))
    print(b[max_index])