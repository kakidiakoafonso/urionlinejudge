def fatorial(n):
    if(n==0):
        return 1
    else:
        return n*(fatorial(n-1))

n = int(input())
if(0<n<13):
    print(fatorial(n))