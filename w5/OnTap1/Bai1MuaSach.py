n = int(input())
V = int(input())

if(n >= 10):
    tien = n*8000*90//100 - V
else:
    tien = n*8000 - V

if(tien > 0):
    print(tien)
else:
    print(0)
