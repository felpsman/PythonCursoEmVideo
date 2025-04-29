primeiro=int(input("Digite o primeiro termo: "))
razao=int(input("Digite a razao da PA: "))
decimo=primeiro+(10-1)*razao
for c in range(primeiro,decimo,razao):
    print("{}".format(c), end=" ")
print("Acabou")