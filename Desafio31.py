quilometros=int(input("Voce ira fazer uma viagem de quantos Km? "))
if quilometros<=200:
    print("O preco da passagem sera de ? R${}".format(quilometros*0.50))
else:
    print("O preco da passagem sera de ? R${}".format(quilometros*0.45))
