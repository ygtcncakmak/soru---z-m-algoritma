def sayi(a,b):
    for i in range(1,a+1):
        b+=str(i)
    return b
a=int(input())
b=""
print(sayi(a,b))