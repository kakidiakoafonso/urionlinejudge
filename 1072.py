n = int(input())
In , out = 0,0
for i in range(n):
    x = int(input())
    if(10<=x<=20):
        In += 1
    else:
        out+=1
print(In,"in")
print(out,"out")