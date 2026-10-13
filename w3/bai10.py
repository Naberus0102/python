a = int(input())
b = int(input())
c = int(input())
d = int(input())

if((a == b and c == d) or (a == c and b == d) or (a == d and b == c)):
    print("YES")
else:
    print("NO")
