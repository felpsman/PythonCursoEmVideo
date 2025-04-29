maioridade=0
menoridade=0
for n in range(7):
    n=int(input("Digite o seu ano de nascimento: "))
    diferenca=2025-n
    if diferenca>18:
        maioridade=maioridade+1
    else:
        menoridade=menoridade+1
print("{} pessoas ja atingiram a maior idade!".format(maioridade))
print("{} pessoas ainda nao atingiram a maior idade!".format(menoridade))
    