d,m,y = map(int,input().split())

if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    nhuan = 1
else:
    nhuan = 0

if(m == 2):
    if(nhuan == 0):
        ngay = 28
    else if(nhuan == 1):
        ngay = 29
else if(m == 4 or m == 6 or m == 9 or m == 11):
    ngay = 30
else:
    ngay = 31

d = d + 1
if d > ngay:
    d = 1
    m = m + 1
if m > 12:
    m = 1
    y = y + 1
print(d,m,y)

