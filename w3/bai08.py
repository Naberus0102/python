# da cho 3 canh hop le nen khong can kiem tra dieu kien

a,b,c = map(int,input().split())

if(a == b and b == c):
    print("Deu")
elif(a == b or c == b or a == c):
    print("Can")
elif(a*a + b*b == c*c or a*a + c*c == b*b or ac*c + b*b == a*a):
    print("Vuong")
else:
    print("Thuong")
