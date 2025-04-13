import random
jokenpo=["Pedra","Papel","Tesoura"]
Mjokenpo=input("O que voce jogou? ")
escolha=random.choice(jokenpo)
if(escolha=="Pedra" and Mjokenpo=="Papel"):
    print("O jogador venceu!")
elif(escolha=="Papel" and Mjokenpo=="Tesoura"):
    print("O jogador venceu!")
elif(escolha=="Tesoura" and Mjokenpo=="Pedra"):
    print("O jogador venceu!")
elif(escolha==Mjokenpo):
    print("Empate!")
else:
    print("O computador Venceu!!")
print(escolha)