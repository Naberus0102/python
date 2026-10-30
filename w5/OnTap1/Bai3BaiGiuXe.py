t = int(input())

if(t < 1):
    print("Khong hop le")
else:
    if(t <= 120):
        tien = 25000
    elif(t <= 300):
        tien = 25000 + 15000*((t - 120 + 59)//60)
    else:
        tien = 25000 + 15000*3 + 20000*((t - 300 + 59)//60)
    print(tien)


