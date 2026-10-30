M = int(input())
g = int(input())

keo = M//g
du = (M % g)

if(keo >= 4):
    them = keo // 4
else:
    them = 0
print(keo+them,du)
