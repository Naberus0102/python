a = int(input())
nam = a//500
hai = (a-nam*500)//200
mot = (a-nam*500-hai*200)//100

print("Số tờ 500:", nam)
print("Số tờ 200:", hai)
print("Số tờ 100:", mot)
