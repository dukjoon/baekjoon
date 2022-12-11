# x = str(input())
# y = str(input())

# a = x.split(':')
# b = y.split(':')
# h_1 = int(a[0])
# m_1 = int(a[1])
# s_1 = int(a[2])

# h_2 = int(b[0])
# m_2 = int(b[1])
# s_2 = int(b[2])

# h_r = 0
# m_r = 0
# s_r = 0

# if h_1 > h_2:
#     h_r = 24 - h_1 + h_2

# else:
#     h_r = h_2 - h_1

# if m_1 > m_2:
#     m_r = 60 - m_2 + m_1
#     h_1 = h_1 - 1

# else:
#     m_r = m_2 - m_1

# if s_1 > s_2:
#     s_r = 60 - s_2 + s_1
#     m_1 = m_1 - 1

# else:
#     s_r = s_2 - s_1

a1,b1,c1=map(int, input().split(":"))
a2,b2,c2=map(int, input().split(":"))
 
ans1=a1*3600+b1*60+c1
ans2=a2*3600+b2*60+c2
if ans1>=ans2 : ans2+=3600*24
ans3=ans2-ans1
a3=ans3//3600
ans3%=3600
b3=ans3//60
ans3%=60
c3=ans3
print("%02d:%02d:%02d"%(a3,b3,c3))