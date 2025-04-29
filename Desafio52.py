num1=int(input("Digite um numero: "))
for n in range(2,num1):
   primo=num1%n
if(num1%num1==0 and num1%1==0 and primo!=0):
    print("O numero {} eh primo!".format(num1))
else:
    print("O numero {} nao eh primo!".format(num1))
