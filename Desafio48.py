soma=0
for n in range(1,501):
    if((n%2==0)==False and n%3==0):
        print(n,end=" ")
        n+=1
        soma+=n
print(soma)