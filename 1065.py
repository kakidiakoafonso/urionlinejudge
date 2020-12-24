# 7 -5 6 -4 12 
c=0
for i in range(5):
    x = int(input())
    if((x%2)==0):
        c+=1
print ("{} valores pares".format(c))