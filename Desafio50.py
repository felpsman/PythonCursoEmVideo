soma=0
for n in range(6):
    num=int(input())
    if(num%2==0):
        soma=soma+num
print("A soma dos valores pares na lista eh: ".format(soma))