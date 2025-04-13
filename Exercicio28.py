import random
lista = [0,1,2,3,4,5]
escolha=random.choice(lista)
chute=int(input("Qual voce aacha que foi o numero escolhido? "))
if chute == escolha:
    print("Parabens, voce acertou!")
else:
    print("Infelizmente voce errou, tente novamente na proxima! O numero escolido foi {}".format(escolha))
