a = int(input())
b = int(input())
c = int(input())
if(a % 2 != 0):
    x = (a + 1)/2
else:
    x = a/2

if(b % 2 != 0):
    y = (b + 1)/2
else:
    y = b/2

if(c % 2 != 0):
    z = (c + 1)/2
else:
    z = c/2
print(int(x+y+z))

