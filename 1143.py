n = int(input())
if(1<n<1000):
    for i in range(1,(n+1)):
        b = i*i
        c = b*i
        print("{} {} {}".format(i,b,c))