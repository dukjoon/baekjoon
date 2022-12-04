# for i in range(0, 3):
#     a, b, c, d, e, f = map(int,input().split())

#     h = d - a
#     m = e - b
#     s = f - c

#     if s < 0:
#         s = s + 60
#         m = m - 1

#         if m < 0:
#             h = h - 1
#             m = m + 60

#     print(h, m, s)

for i in range(3):
    in_h, in_m, in_s, out_h, out_m, out_s = map(int, input().split())
    time = (out_h * 3600 + out_m * 60 + out_s) - (in_h * 3600 + in_m * 60 + in_s)
    print(time // 3600, (time % 3600) // 60, (time % 3600) % 60)
