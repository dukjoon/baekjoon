a = str(input())

r = a.split("/")

if int(r[0]) + int(r[2]) < int(r[1]):
    print("hasu")
elif int(r[1]) == 0:
    print("hasu")
else:
    print("gosu")