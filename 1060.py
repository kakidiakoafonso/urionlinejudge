par,impar, pos, neg = 0,0,0,0
for i in range(5):
    x = int(input())
    if((x%2)==0):
        par+=1
        if(x==0):
            continue
        elif(x>0):
            pos+=1
        else:
            neg+=1
    else:
        impar+=1
        if(x>0):
            pos+=1
        else:
            neg+=1
print ("{} valor(es) par(es)".format(par))
print ("{} valor(es) impar(es)".format(impar))
print ("{} valor(es) positivo(s)".format(pos))
print ("{} valor(es) negativo(s)".format(neg))