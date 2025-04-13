casa=float(input("Qual o valor da casa? "))
salario=float(input("Qual o seu salario? "))
Qanos=int(input("Quantos anos ele ira pagar? "))
prestacao=casa/(Qanos*12)
minimosalario=salario*0.30
if(prestacao<=minimosalario):
    print("Emprestimo aceito!")
else:
    print("Emprestimo Negado!")

