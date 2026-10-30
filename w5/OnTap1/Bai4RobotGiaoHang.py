x,y,k = map(int,input().split())

# if((x + y == k) or ((k- x - y) % 2 == 0 and (k - x - y) > 0)):
#     print("YES")
#
# else:
#     print("NO")

z = abs(x) + abs(y)
if(k >= z and (k - z) % 2 == 0):
    print("YES")
else:
    print("NO")
