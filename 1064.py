# 7 -5 6 -3.4 4.6 12 = 7.4
c=0
pos = 0
for i in range(6):
    x = float(input())
    if(x>0):
        c+=1
        pos+=x
media = pos/c
print ("{} valores positivos".format(c))
print ("{0:.1f}".format(media))