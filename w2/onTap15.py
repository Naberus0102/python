sec = int(input())
s = sec % 60

m = sec//60
mi = m%60

h = m//60
ho = h%24

day = h//24
print(day,ho,mi,s,sep = ":")
