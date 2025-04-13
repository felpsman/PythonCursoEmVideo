x=int(input("Qual era a velocidade do motorista? "))
multa=(7*(x-80))
if x>80:
    print("O motorista foi multado! A multa eh no valor de: R${}".format(multa))
else:
    print("O motorista nao levou multa! Parabens!")