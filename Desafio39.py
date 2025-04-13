nascimento=int(input("Qual o ano de seu nascimento? "))
Estanahora=2025-nascimento
if(Estanahora==18):
    print("Esta na hora de se alistar!")
elif(Estanahora<18):
    print("Voce ainda vai se alistar, mas nao agora! Ainda falta {} anos!".format(18-Estanahora))
else:
    print("Ja passou da hora de se alistar, se aliste o mais rapido possivel! Ja se passaram {} anos!".format(Estanahora-18))
