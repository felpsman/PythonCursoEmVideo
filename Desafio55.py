maiorpeso=0
for peso in range(5):
    peso=float(input("Digite o seu peso: "))
    if(peso>maiorpeso):
        maiorpeso=peso
print("O maior peso eh {}".format(maiorpeso))