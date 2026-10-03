
sec = int(input())
s = sec % 60

m = sec//60
mi = m%60

h = m//60
print(h,mi,s,sep = ":")
