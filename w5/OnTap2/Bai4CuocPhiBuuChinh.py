m,L,W,H,s = map(int,input())

v = (L*W*H + 4990)//5000 #LAM TRON DEN HANG NGUYEN
w = max(m,v)

if w <= 2:
    cuoc = 30000;
else if w <= 10:
    cuoc = 30000 + (w - 2)*7000
else:
    cuoc = 86000 + (w - 11)*5000

if(s == 0):
    cuocMoi = cuoc
else if(s == 1):
    cuocMoi = cuoc*130//100
else:
    print("Khong hop le")

print(cuocMoi)
