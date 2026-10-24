x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

if((x1 >= 1 and x1 <= 8) and (y1 >= 1 and y1 <= 8) and (x2 >= 1 and x2 <= 8)  and (y2 >= 1 and y2 <= 8) and (x1 == x2 or y1 == y2)):
    print("YES")
else:
    print("NO")
