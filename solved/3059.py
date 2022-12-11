import sys
for _ in range(int(sys.stdin.readline())):
    s=(sys.stdin.readline())
    tmp=[0]*26
    cnt=0
    for i in range(len(s)-1):
        tmp[ ord (s[i])-65  ]=1
    for i in range( len (tmp)):
        if tmp[i]==0:cnt+=65+i
    print(cnt)