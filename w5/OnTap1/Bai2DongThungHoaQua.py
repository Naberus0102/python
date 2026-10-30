m = int(input())

a = m//10
du = m - 10*a
b = du//3

if(du % 3 != 0):
    b = b+1

print(a,b)
