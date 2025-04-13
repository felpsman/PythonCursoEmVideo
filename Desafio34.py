salario=float(input("Qual eh o seu salario? "))
aumento1=(salario*0.10)+salario
aumento2=(salario*0.15) + salario
if salario >=1250:
    print("O seu novo salario sera R${}! Um aumento de R${}".format(aumento1,salario*0.10))
else:
    print("O seu novo salario sera R${}! Um aumnento de R${}".format(aumento2,salario*0.15))